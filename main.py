import tensorflow as tf
from model_3dgan import GAN3D

with tf.Session() as sess:
    train_data_path = 'dataset/bathtub'
    checkpoint_dir = 'checkpoints'
    sample_g_path = 'generated/baththub'  # should be for the test

    gan3d = GAN3D(sess=sess, data_set_path=train_data_path,
                   checkpoint_dir=checkpoint_dir, sample_g_path=sample_g_path)

    gan3d.train()
