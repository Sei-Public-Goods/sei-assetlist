# Sei Assetlist
This repository provides a publicly maintained registry of assets on Sei.

## Contributing
We encourage all creators on Sei to contribute any tokens or assets to this repository. To propose changes directly, you can open a Pull Request against this repository.

1. [Fork the repository](https://guides.github.com/activities/forking/), then [clone](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project#cloning-a-fork) the forked repository locally.
2. Make changes to the repository. Ensure that your changes confirm to the contribution guides below.
3. Commit and push your changes to your forked repository.
4. Once your changes have been pushed to your forked repository, [make a Pull Request](https://git-scm.com/downloads) against this repository.

### Schema
Each `json` in this repository should follow a specific schema. Refer to the schemas for each file in the `./schema/` directory for details about how each field should be formatted.
## Querying
To query the files in the assetlist directly, you can make call github directly (eg. https://raw.githubusercontent.com/Sei-Public-Goods/sei-assetlist/main/assetlist.json).

Alternatively, you can query the sei-app-api (GET app-api.seinetwork.io/assetList)