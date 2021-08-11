---
sort: 2
---
# Edge Deployment Technology Selection Criteria

1. Use Case – Why Edge?:
    * Custom model deployments v. End to end solution, e.g.: Instore security – Verkada etc. 
    * Faster inferencing – closer to source?
    * Data residency? 
    * Model should be able to run if connection to Azure is lost?
    * Target site has limited to zero internet connectivity?
2. Target compute type (also informed by customer skills maturity): 
    * VM  -> IOT Edge? ARC for VMs?
    * K8s - > Arc for K8s?
3. HA and DR requirements for edge models:
    * Criteria? SLAs etc. 
4. Azure Parity requirements:
    * AAD / AD integration?
    * Storage or other PaaS support
5. Target compute spec requirements:
    * CPU, GPU, FPGA?
    * Infrastructure is custom or MS edge offerings like Stack Edge, Stack Hub, HCI
    * Custom hardware like Percept
6. Support for specific model frameworks:
    * Intel LVA? Vino? 
