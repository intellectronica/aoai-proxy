## Azure Open AI Proxy

In complex, distributed scenarios, we may have the need to multiplex between multiple Open AI clients and multiple Azure Open AI deployments. In addition, it would be good to be able to track and attribute the cost of the requests per user and/or endpoint.

This does exactly that, by creating a simple proxy HTTP server that sits between the client the Azure Open AI endpoint, dispatches the request to one of several endpoints, and tracks the usage and cost after each request.

See [notebook](aoai-proxy.ipynb).
