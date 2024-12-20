Mesoscopic Insights: Orchestrating Multi-scale & Hybrid Architecture for Image Manipulation Localization
========

This repository contains the official PyTorch implementation of our AAAI2025 paper: ["Mesoscopic Insights: Orchestrating Multi-scale & Hybrid Architecture for Image Manipulation Localization"](https://arxiv.org/abs/2412.13753).

## Test

This document provides step-by-step instructions for setting up the environment for the project, ensuring compatibility and successful installation of required dependencies.

### 1. Clone Project

```bash
git@github.com:scu-zjz/Mesorch.git
```

### 2. Create and Activate Conda Virtual Environment

Run the following command in your terminal:

```bash
conda create -n mesorch python==3.10
conda activate mesorch
pip install torch torchvision
pip install imdlbenco
pip install "numpy<2"
```

### 3. Download the Pretrained Checkpoints

To use the pretrained models, download the checkpoints from the following link:

[Google Drive](https://drive.google.com/drive/folders/1jwYv-S3HAZqzz0YxM9bJynBiPv-O9-6x?usp=sharing)
[Baidu Drive](https://pan.baidu.com/s/13Byzl5kFc_vZHX8SNe6gGg?pwd=meso)

#### Directory Structure

The directory structure of the checkpoints is as follows:

```plaintext
Mesorch/
├── ckpt_mesorch/
│   └── mesorch-98.pth
├── ckpt_mesorch_p/
│   └── mesorch_p-118.pth
├── extractor/
├── .gitignore
├── balanced_dataset.json
├── LICENSE
├── ...
├── train_mesorch_p.sh
├── train_mesorch.sh
└── train.py
```


### 4. Run tests

All the following examples are based on the **Mesorch** model. The **Mesorch-P** model shares the same testing procedure as Mesorch, with no significant differences.

#### 4.1 Standard F1

```bash
sh test_mesorch_f1.sh
```

#### 4.2 Permute F1

```bash
sh test_mesorch_permute_f1.sh
```

#### 4.3 Robust test

```bash
sh test_robust_mesorch.sh
```

## Training Instructions

This part provides instructions on how to configure and execute the training shell script for this project.
### 1. Segformer Pretrained File Download

To begin the training process, you need to download the pretrained weights for Segformer. Specifically, this project uses the **mit-b3** model pretrained on ImageNet. Follow the instructions below to download it from the official Segformer GitHub repository:

1. Visit the official Segformer GitHub repository: [Segformer GitHub](https://github.com/NVlabs/SegFormer).

2. Navigate to the **"Training"** section in the repository's README or directly access the download link provided for the **mit-b3** model.

3. Download the pretrained weights for **mit-b3**.
 
### 2. Configure Parameters

To start the training process, you need to execute the provided `.sh` shell script file. Before running the script, ensure that key parameters such as `seg_pretrain_path`, `data_path`, and `test_data_path` are properly configured.

Before running the training shell script, edit and configure the following parameters in the `.sh` file as needed:

- **`seg_pretrain_path`**: This should point to the pretrained segmentation model file. Ensure the file exists at the specified location.

  Example:

  ```bash
  seg_pretrain_path="/mnt/data0/xuekang/workspace/segformer/mit_b3.pth"
  ```

- **`data_path`**: This is the directory containing the training data. Update this path to the location of your training dataset

  Example:

  ```bash
  data_path="/mnt/data0/xuekang/workspace/Mesorch/balanced_dataset.json"
  ```

- **`test_data_path`**: This is the directory containing the testing data. Update this path to the location of your test dataset.

  Example:

  ```bash
  test_data_path="/mnt/data0/public_datasets/IML/CASIA1.0"
  ```

### 3. **Run the Training Script**

Once the parameters are correctly configured, execute the shell script to start the training process. Use the following command:

```bash
sh train_mesorch.sh
```

## Citation​
If you find our work interesting or helpful, please don't hesitate to give us a star🌟 and cite our paper🥰! Your support truly encourages us!
```bibtex
@misc{zhu2024meso
      title={Mesoscopic Insights: Orchestrating Multi-scale & Hybrid Architecture for Image Manipulation Localization}, 
      author={Xuekang Zhu and Xiaochen Ma and Lei Su and Zhuohang Jiang and Bo Du and Xiwen Wang and Zeyu Lei and Wentao Feng and Chi-Man Pun and Jizhe Zhou},
      year={2024},
      eprint={2412.13753},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2412.13753}, 
}
```



