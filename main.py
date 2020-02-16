import argparse
from home import Home

parser = argparse.ArgumentParser(description='Change the lights.')
parser.add_argument('Scene', nargs=1,
                    help='The name of the light scene to switch to')

args = parser.parse_args()

state = args.Scene[0]
house = Home()
house.set_state(state)