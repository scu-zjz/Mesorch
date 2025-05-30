Mesoscopic Insights: Orchestrating Multi-scale & Hybrid Architecture for Image Manipulation Localization
========

This repository contains the official PyTorch implementation of our AAAI2025 paper: ["Mesoscopic Insights: Orchestrating Multi-scale & Hybrid Architecture for Image Manipulation Localization"](https://arxiv.org/abs/2412.13753).


![Mesorch Framework](images/mesorch.png)  
The Mesorch Framework employs a novel multi-scale parallel architecture to effectively process input images, setting a new benchmark in image manipulation localization. By leveraging distinct frequency components and feature hierarchies, it captures both local manipulations and global inconsistencies. Its adaptive weighting mechanism ensures precise and comprehensive results, making it a robust solution for image manipulation localization tasks.



**Note:**  
All code in this project is developed based on the [IMDLBenCo](https://github.com/scu-zjz/IMDLBenCo) repository. 

For any dataset-related issues or additional resources, please refer to the repository linked above.

Below are the testing and training details for Mesorch based on this repository.

## Testing Instructions
<details>
<summary><b>Click to expand</b></summary>



This document provides step-by-step instructions for setting up the environment for the project, ensuring compatibility and successful installation of required dependencies.

### 1. Clone Project

```bash
git clone git@github.com:scu-zjz/Mesorch.git
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
</details>

## Training Instructions
<details>
<summary><b>Click to expand</b></summary>


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

**Note:** If you experience connectivity issues with Huggingface, you can set the following environment variable to use an alternative endpoint:

```bash
export HF_ENDPOINT="https://hf-mirror.com"
```

</details>

## Citation
If you find our work interesting or helpful, please don't hesitate to give us a star🌟 and cite our paper🥰! Your support truly encourages us!
```bibtex
@inproceedings{zhu2025mesoscopic,
  title={Mesoscopic insights: orchestrating multi-scale \& hybrid architecture for image manipulation localization},
  author={Zhu, Xuekang and Ma, Xiaochen and Su, Lei and Jiang, Zhuohang and Du, Bo and Wang, Xiwen and Lei, Zeyu and Feng, Wentao and Pun, Chi-Man and Zhou, Ji-Zhe},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={39},
  number={10},
  pages={11022--11030},
  year={2025}
}
```
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=scu-zjz/mesorch&type=Date)](https://www.star-history.com/#scu-zjz/mesorch&Date)


