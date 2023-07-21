from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="01_config.yaml", dry_run=True)

results = nr.run(task=napalm_get, getters=["facts", "interfaces", "config"])

print_result(results)
