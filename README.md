# PyTorch_Device_Agnostic_Code
Simple PyTorch device agnostic code for setting up GPU.

Create for my personal use. Since I use macOS and Linux server with NVIDIA GPU this code supports "MPS" and "CUDA".

# How to use
* Download this code
* Import this code like below
    ```python
    import get_default_device
    ```

* And check what GPU you're using
    ```python
    device = get_default_device()
    ```

## To-dos
* Adding code for multiple GPU
