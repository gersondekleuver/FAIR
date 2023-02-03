import numpy as np
import sys
from src.mgr import manager
from src.dataset_loader import init_dataset
from src.services import init_service
import torch
import random
import os
import ray
import lib
from lib import init_proto_model

# Ray Initialization
# num_cpus = os.cpu_count()
# ray.init(num_cpus = num_cpus)


def main(runName):
    # make change to your task for fact project
    if runName is None:
        assert "please pass runName"

    print("Your are running %s"%runName)


    if runName in ("teacher_Resnet50", "student_Resnet18" ):
        serviceType ="recognition"
    elif runName in ("kd_Resnet50_18" ):
        serviceType ="kd"
    elif runName in ("eval_setting" ):
        serviceType ="evaluate"
    else:
        raise Exception("wrong runName %s" %runName )


    newRun = "false"
    randomRun =  "org"
    ablationType = "Resnet50_18_cars"

   
    if runName.strip().lower() == "none":
        runName = None

    print(runName, newRun, serviceType, randomRun, ablationType)

    newRun = newRun.lower() == "true"
    if runName.strip().lower() == "none":
        runName = None
    manager(runName, newRun, serviceType, randomRun, ablationType)

    # Fix Randomness
    seed = manager.settingsConfig.train.seed
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)

    dataset_loader = init_dataset(manager.dataConfig.loaderName)
    #service = init_service(serviceType, manager.service_name, dataset_loader)
    #service()
    model = init_proto_model(manager, dataset_loader.classes, manager.settingsConfig.backbone)[0]

    if runName in ("teacher_Resnet50"):
        converted_name = "teacher_converted.pkl"
    elif runName in ("student_Resnet18" ):
        converted_name = "student_converted.pkl"
    elif runName in ("kd_Resnet50_18" ):
        converted_name = "kd_converted.pkl"
    else:
        raise Exception("wrong runName %s" %runName)

    torch.save(model, f"./converted_models/{converted_name}")

if __name__ == "__main__":
    runName = "teacher_Resnet50"
    main(runName)
