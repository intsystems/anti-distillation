import torch 
data_path = './data/'
num_workers = 2
batch_size = 256
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using {} device'.format(device))

colab_path = '/content/drive/MyDrive/models/'
local_path = './models/'
use_colab = True 

num_repeats = 5


full_teacher_training_epochs = 50
full_student_training_epochs = 50
full_teacher_learning_rate = 1e-4 
full_student_learning_rate = 1e-4 

teacher_5_training_epochs = 30
student_5_training_epochs = 30
teacher_5_learning_rate = 1e-4
student_5_learning_rate = 1e-4 

student_5_antidistil_epochs = 15
student_5_antidistil_learning_rate = 1e-4 

noise_eps = [i/100 for i in range(10)]

fsgm_eps = [i/500 for i in range(10)]

teacher_blocks = [128, 64, 32]
student_blocks =  [256, 128, 64]
