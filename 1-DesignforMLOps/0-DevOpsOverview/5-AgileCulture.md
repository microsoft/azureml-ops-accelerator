---
sort: 6
---
# Adopting an Agile culture
**Source**: [Adopting an Agile culture](https://docs.microsoft.com/en-us/devops/plan/adopting-agile)

If there's one lesson to be learned from the last decade of "Agile transformations", it's that there is 
no one-size-fits-all solution to adopting or implementing an [Agile](https://docs.microsoft.com/en-us/devops/plan/what-is-agile) approach. Every 
organization has different needs, constraints, and requirements. Blindly following prescription won't 
lead to success.

The Agile movement is about continually finding ways to improve the approach and practice of building 
software. It's not about a perfect daily standup or retrospective. Instead, it's about creating a culture 
where the right thing happens more often than not. Activities like standups and retrospectives have their 
place, but they won't change an organization's culture.

![Agile culture](https://raw.githubusercontent.com/microsoft/azureml-ops-accelerator/main/1-DesignforMLOps/0-DevOpsOverview/_img/agile-culture.png)

This article details foundational elements that every organization needs to create an Agile mindset and 
culture. They should not be followed blindly, but rather apply what makes sense in a given environment.

## Schedule and rhythm

It's important to understand that there is no perfect sprint length. Teams have been successful with 
different sprint lengths ranging from 1-4 weeks. What really matters is consistency.

Select a sprint length that works for an organization's culture, product, and  desire to provide updates. 
For example, the Developer Tools division at Microsoft (roughly 6,000 people) works in three-week sprints.
The choice of a three-week sprint wasn't made by the leadership team or other managers; it came from 
direct feedback from the engineering teams. The entire division operates on this three-week sprint 
schedule. The sprints have since become the _heartbeat_ of the organization. Now every team is marching 
to the beat of the same drum.

It's important to pick a sprint length and stick with it. If there are multiple Agile teams, they should 
all use the same sprint length. If feedback drives a change, then be receptive. It will become clear when
the right term is in place.

## A culture of shipping

[Peter Provost](https://twitter.com/pprovost) said "You can't cheat shipping". The simplicity and truth 
of that statement is a cornerstone of Agile culture. What Peter means is that shipping your software will
teach you things that you can't and won't understand; unless you're actually shipping your software.

Human nature is to delay or avoid doing things until absolutely necessary. This couldn't be more true 
when it comes to software development. Teams punt bugs to the end of the cycle, don't think about setup or
upgrade until they're forced to, and typically avoid things like localization and accessibility wherever
possible. When this pattern emerges, teams are building up technical debt that will need to be paid down 
at a later time. Shipping demands all debt be paid. You can't cheat shipping. To establish an Agile 
culture, start by trying to ship the product at the end of every sprint. It won't be easy at first, but
when a team attempts it, they quickly discover all the things that should be happening, but aren't.

## Healthy teams

There is no recipe for the perfect Agile team. However, there are a few key characteristics that make
success for an Agile team much easier to achieve.

### Co-locate teams whenever possible

Can a team find success with people spread out across different geographies? Of course, but it's more
difficult. When people are co-located and sitting in the same room, the right conversations just tend 
to happen. It's still possible to succeed with teams located across globe and different time zones.
But wouldn't that same team have an advantage without all of those obstacles?

### Keep teams intact for a reasonable length of time

Allow teams to master the art of building software together. When teams are scrambled, it disrupts any
chemistry they may have developed. There are times when it's appropriate to reorganize teams. However,
teams typically work better when they're given time to learn how to work together. As a guideline, try
to keep teams intact for at least twelve months.

### Load balance work, not people

Sometimes teams fall behind and need help. A common tactic to address this is to lend a person from one 
team to another. However, that can be counterproductive. A better solution is to load balance work to 
another team, rather than load-balancing people between them. Pulling a person off of one team to help
another disrupts both teams and can frustrate the person being moved, even if temporary. All of this 
impacts team productivity and, more likely than not, negatively impacts the ability to get back on schedule.

Load balancing work to another team allows a team that is already established to step in and help out. 
It becomes a _priority_ conversation and not a _people_ conversation.

## Teams should own feature areas, not layers of architecture

Strive to build vertical teams that own feature areas. These teams are responsible for all the work 
required to add features to their area, from database to user interface changes. The team is empowered 
to deliver and own an end-to-end experience.

Horizontal teams that own a layers of architecture means no single team is responsible for the end-to-end 
experience. Adding a feature requires multiple teams to coordinate and requires a higher level of 
dependency management. Resolving bugs requires multiple teams to investigate whether they own the code 
required to fix the bug. Bugs are batted around as teams determine it's *not their bug* and assign it to 
another team.

Feature teams don't have these issues. Ownership and accountability is clear. There may be a place for 
some architectural based teams. However, the more vertically focused teams are, the more effective they
will be.

## Next steps

As teams embark on their own Agile transformation, keep these foundational principles in mind. And 
remember, there is no single recipe that will work for every organization. Agile transformations are a 
journey. Make changes and learn from them. Over time the organization will develop the Agile culture it 
needs.
