This a a CartPole test environment
Usage:

first cd into this folder and do pip install -e . to install this environment 

in your Python code, do

import gym
import gym_cp

env = gym.make('cp-v0')

Now, this re-creates the original CartPole environment parameters.

To change the parameters do:

env.my_init(G=9.8,MC=1,MP=0.1,L=0.5,F=10) #these are the default params of the environment

NOTE: Do env = env.unwrapped before doing env.my_init .. else you will face some 'TimeLimit' error

where G= gravity, MC= Mass of Cart, MP = Mass of Pole, L= Length of pole, F = Magnitude of force applied to the cart

This will change the corresponding values. You can also choose to update only a few params, say only G and MC. the rest will kept to the default values internally

You can choose to call my_init even every episode to change these parameters
