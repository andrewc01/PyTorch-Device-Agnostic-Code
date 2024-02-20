# PyTorch Device Agnostic Code
Simple PyTorch device agnostic code for setting up GPU.

Create for my personal use and since I use macOS and Linux server with NVIDIA GPU, this code supports "MPS", "CUDA" and "CPU" for default.

# How to use
* Download this code
* Import this code like below
    ```python
    from device_agnostic_code import get_default_device
    ```

* And check what GPU you're using
    ```python
    device = get_default_device()
    device
    ```

## To-dos
* Adding code for multiple GPU
* Make helper python file
