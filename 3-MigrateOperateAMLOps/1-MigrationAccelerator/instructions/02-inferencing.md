# Inferencing

## Preparing the real-time inferencing code

1. Adapt conda enviroment for inferencing
    * Copy your dependencies from [`aml_config/train-conda.yml`](../models/model1/aml_config/train-conda.yml) to [`aml_config/inference-conda.yml`](../models/model1/aml_config/inference-conda.yml)
    * If you have different dependencies for inferencing, you can adapt them in [`aml_config/inference-conda.yml`](../models/model1/aml_config/train-conda.yml)

1. Adapt existing `score.py`
    * Open [`score.py`](../models/model1/score.py) and start updating the `init()` and `run()` methods following the instructions given in the file
    * Updating `init()`:
        * The `init` method is executed once the real-time scoring service is starting up and is usually used to load the model
        * The model file(s) are automatically injected by AML and the location is available in the environment variable `AZUREML_MODEL_DIR`
        * For more details look at the existing [`score.py`](../models/model1/score.py)
    * Updating `run()`:
        * The `run` method is executed whenever a `HTTP POST` request is received by the service
        * The input to the method is usually JSON, which can be processed and then passed into your model
        * For more details look at the existing [`score.py`](../models/model1/score.py)
        * If you want to receive binary data, e.g., images, you can try use the following code (full example [here](https://github.com/csiebler/unet-pytorch-azureml/blob/master/model/score.py)):
        ```python
        from azureml.contrib.services.aml_request import AMLRequest, rawhttp
        from azureml.contrib.services.aml_response import AMLResponse
        ...
        @rawhttp
        def run(request):
            if request.method == 'POST':
                request_body = request.get_data(False)
                input_image = Image.open(io.BytesIO(request_body))

                # Do something with the input image
                response = 42 # create a more meaningful response

                headers = {
                    'Content-Type': 'image/png' # Set your Content-Type of the response
                }
                
                return AMLResponse(response, 200, headers)
            if request.method == 'GET':
                response_body = str.encode("GET is not supported")
                return AMLResponse(response_body, 405)
            return AMLResponse("Bad Request", 500)
        ```
    * You can test your `score.py` script locally using (make sure the file `outputs/model.pkl` exists):
    ```
    pytest tests/
    ```

## Running real-time inferecing locally

1. Deploy model as a RESTful service to local host 
    * Deploy locally to Docker:
    ```
    az ml model deploy -n test-deploy -m demo-model:1 --ic aml_config/inference-config.yml --dc deployment/deployment-config-aci.yml --runtime python --compute-type local --port 32000 --overwrite
    ```
    * The model is referenced by `model_name:model_version` (in this case `demo-model` with version `1`)

1. Test if the model works
    * To test the model, `POST` a sample request to your local endpoint using a tool of you choice
    * *Option 1* - Test using VSCode with `rest-client`
      * Install the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for VSCode
      * Open [`local-endpoint.http`](../models/model1/tests/local-endpoint.http) in VSCode and click `Send Request`
    * *Option 2* - Use the tool of your choice, e.g., Postman, using the following request structure:
    ```
    POST http://localhost:32000/score HTTP/1.1
    Content-Type: application/json

    { 
        "data": [
            {
            "Age": 20,
            "Sex": "male",
            "Job": 0,
            "Housing": "own",
            "Saving accounts": "little",
            "Checking account": "little",
            "Credit amount": 100,
            "Duration": 48,
            "Purpose": "radio/TV"
            }
        ]
    }
    ```
    * You can access the automatically generated Swagger definition at `http://localhost:32000/swagger.json`
    * Once it is working, you can delete the locally deployed service:
    ```
    az ml service delete --name test-deploy
    ```

## Running real-time inferecing on Azure

1. Deploy model to ACI (Azure Container Instances) for testing the model in Azure
    * Finally, you can test deploying the model to ACI:
    ```
    az ml model deploy -n test-deploy-aci -m demo-model:1 --ic aml_config/inference-config.yml --dc deployment/deployment-config-aci.yml --overwrite
    ```
    * Test using VSCode with `rest-client` (same as above)
      * In the AML Studio UI, goto `Endpoints -> test-deploy-aci -> Consume` and note the `REST endpoint` and `Primary key`
      * Open [`aci-endpoint.http`](../models/model1/tests/aci-endpoint.http) in VSCode, update your `URL` and `Authorization key`:
      ```
      POST http://d42afe74-eb70-4dc0-adb9-xxxxxxxxx.westeurope.azurecontainer.io/score HTTP/1.1
      Content-Type: application/json
      Authorization: Bearer xxxxxxxxxxxxxx
      ```
    * You can delete the deployment via:
    ```
    az ml service delete --name test-deploy-aci
    ```

1. Deploy model to AKS (Azure Kubernetes Service)
    * First, create a new dev/test AKS cluster (single node cluster):
    ```
    az ml computetarget create aks --name aks-cluster --vm-size Standard_D3_v2 --cluster-purpose DevTest
    ```
    * Finally, you can test deploying the model to AKS:
    ```
    az ml model deploy -n test-deploy-aks --ct aks-cluster -m demo-model:1 --ic aml_config/inference-config.yml --dc deployment/deployment-config-aks.yml --overwrite
    ```
    * Test using VSCode with `rest-client` (same as above)
      * In the AML Studio UI, goto `Endpoints -> test-deploy-aks -> Consume` and note the `REST endpoint` and `Primary key`
      * Open [`aks-endpoint.http`](../models/model1/tests/aks-endpoint.http) in VSCode, update your `URL` and `Authorization key`:
      ```
      POST http://url-to-your-aks-endpoint/score HTTP/1.1
      Content-Type: application/json
      Authorization: Bearer xxxxxxxxxxxxxx
      ```
    * You can delete the deployment via:
    ```
    az ml service delete --name test-deploy-aks
    ```

Great, the model is running a service, let's move on the [next section](03-pipelines.md) and look how we can run ML Pipelines for automation on Azure.
