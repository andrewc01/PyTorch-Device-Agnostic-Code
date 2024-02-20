import torch

def get_default_device():
    if torch.cuda.is_available():
        return torch.device('cuda') # nvidia gpu
    elif torch.backends.mps.is_available():
        return torch.device('mps') # apple silicon gpu
    else:
        return torch.device('cpu') # default