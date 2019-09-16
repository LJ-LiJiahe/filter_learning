from torch import nn
from torchvision import transforms


# Directories
data_folder = "data/"
train_input_dir = "train_input"
train_target_dir = "train_target"
test_input_dir = "test_input"
test_target_dir = "test_target"
validate_input_dir = "test_input"
validate_target_dir = "test_target"
loss_folder = "loss"

transform = None

train_batch_size = 50
test_batch_size = 1
train_shuffle = False
test_shuffle = False

criterion = nn.MSELoss()
lr = 0.001


epoch = 1000
save_epoch = 5

# Model
recov_from_ckpt = False
ckpt_folder = "checkpoints"

# Model
in_channels = 3
out_channels = 10
kernel_size = 3
stride = 1
padding = 1


# Filter
filter_in_channels = 1
filter_out_channels = 1
filter_kernel_size = 3
filter_stride = 1
filter_padding = 1
filter_bias = False
filter_transform = transforms.Compose([
    transforms.functional.to_grayscale(num_output_channels=1),
    transforms.ToTensor()])