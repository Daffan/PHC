# Quick steps to start

## Prepare dataset
* Follow 3 in (https://github.com/Daffan/PHC?tab=readme-ov-file#dependencies) to download the SMPL model.
* Follow 4 in (https://github.com/Daffan/PHC?tab=readme-ov-file#dependencies) to download the sample data. You can use the sample data to quickly start some training.

## Quick training:
We can try PHC+: rotation + keypoint model, can getup from the ground but not walk back -- model used in PULSE due to time constraint
```
python phc/run_hydra.py learning=im_mcp_big  exp_name=phc_comp_3 env=env_im_getup_mcp robot=smpl_humanoid env.zero_out_far=False robot.real_weight_porpotion_boxes=False env.num_prim=3 env.motion_file=sample_data/amass_isaac_standing_upright_slim.pkl env.models=['output/HumanoidIm/phc_3/Humanoid.pth'] env.num_envs=1  headless=False epoch=-1 test=True
```

## Prepare AMASS dataset
Check the instruction here: https://github.com/Daffan/PHC?tab=readme-ov-file#training

AMASS dataset is a collection of multiple different dataset. You need to download them one by one.

Once you download them all:
```
python scripts/data_process/convert_amass_data.py
```

Once the dataset is processed. You can train a model using just MLP. Motion file should be replaced with the entire AMASS dataset.
```
python phc/run_hydra.py learning=im_big exp_name=phc_prim env=env_im robot=smpl_humanoid env.motion_file=sample_data/amass_isaac_standing_upright_slim.pkl 
```