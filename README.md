# ArquiCompTarea2
Tarea 2 \
Primero conseguimos las API Keys de https://openweathermap.org y de https://api.cmfchile.cl/documentacion \
Luego las colocamos en python3-fn/handler.py en las urls correspondientes.\
Luego ejecutamos los siguientes comandos con docker y kubernetes corriendo: \
<ul>
<li> curl-sSL https://cli.openfaas.com sudo -E sh </li>

<li>kubectl port-forward svc/gateway -n openfaas 31112:8080 </li>

<li>export OPENFAAS_URL=http://127.0.0.1:31112 </li>

<li>export PASSWORD={passworddeopenfaas} </li>

<li>echo -n SPASSWORD | faas-cli login —password-stdin </li>

<li>faas-cli build -f python3-fn. yml </li>

<li>faas-cli push -f python3-fn. yml </li>

<li>faas-cli deploy -f python3-fn. yml </li>
</ul>
