import asyncio
from controller import Robot, Motor

async def wait(delay):

    await asyncio.sleep(delay)

async def crouch(robot, velocity=0.5):

    # Motor Names
    motors = {}
    motor_names = [
        "AnkleL", "AnkleR",
        "LegLowerL", "LegLowerR",
        "LegUpperL", "LegUpperR",
        "ShoulderL", "ShoulderR",
        "ArmUpperL", "ArmUpperR"
    ]

    for name in motor_names:
        motors[name] = robot.getMotor(name)

    # Crouch positions
    crouch_positions = {
        "LegLowerL": 0.8,
        "LegLowerR": -0.8,
        "LegUpperL": -1.5,
        "LegUpperR": 1.5,
        "AnkleL": 0.4,
        "AnkleR": -0.4,
        "ShoulderL": -1.3,
        "ShoulderR": 1.3,
        "ArmUpperL": 1.5,
        "ArmUpperR": -1.5
    }

    # Setters
    for name, position in crouch_positions.items():
        motors[name].setPosition(position)
        motors[name].setVelocity(velocity)
        print("Crouching...")

async def reach_out_and_grab(robot, velocity=0.3):

    # Motor Names
    motors = {}
    motor_names = ["ArmLowerL", "ArmLowerR"]

    for name in motor_names:
        motors[name] = robot.getMotor(name)

    # Arm positions
    reach_positions = {
        "ArmLowerL": -0.3,
        "ArmLowerR": 0.3
    }

    # Setters
    for name, position in reach_positions.items():
        motors[name].setPosition(position)
        motors[name].setVelocity(velocity)
        print("Reaching out and grabbing...")

async def stand(robot, velocity=100):

    # Motor Names
    motors = {}
    motor_names = [
        "AnkleL", "AnkleR",
        "LegLowerL", "LegLowerR",
        "LegUpperL", "LegUpperR",
        "ShoulderL", "ShoulderR",
        "ArmUpperL", "ArmUpperR"
    ]
    for name in motor_names:
        motors[name] = robot.getMotor(name)

    # Stand positions
    stand_positions = {
        "AnkleL": 0.0,
        "AnkleR": 0.0,
        "LegLowerL": 0.0,
        "LegLowerR": 0.0,
        "LegUpperL": 0.0,
        "LegUpperR": 0.0,
    }

    # Setters
    for name, position in stand_positions.items():
        motors[name].setPosition(position)
        motors[name].setVelocity(velocity)
        print("Standing up...")

async def hands_behin_head(robot, velocity=0.3):

    # Motor Names
    motors = {}
    motor_names = ["ShoulderL", "ShoulderR"]

    for name in motor_names:
        motors[name] = robot.getMotor(name)

    # shoulder positions
    hand_positions = {
        "ShoulderL": -5,
        "ShoulderR": 5
    }

    # Setters
    for name, position in hand_positions.items():
        motors[name].setPosition(position)
        motors[name].setVelocity(velocity)
        print("Ready to throw...")

async def throw(robot, velocity=5):

    # Motor Arms
    motors = {}
    motor_names = ["ShoulderL", "ShoulderR",
                   "ArmUpperL", "ArmUpperR", "AnkleL", "AnkleR",]

    for name in motor_names:
        motors[name] = robot.getMotor(name)

    # Throwing positions
    throw_positions = {
        "ShoulderL": 2.8,
        "ShoulderR": -2.8,
        "ArmUpperL": 0.3,
        "ArmUpperR": -0.3,
    }

    # Setters
    for name, position in throw_positions.items():
        motors[name].setPosition(position)
        motors[name].setVelocity(velocity)
        print("throwing")


async def reset_positions(robot, velocity=0.3):

    # Motor Names
    motors = {}
    motor_names = [
        "AnkleL", "AnkleR",
        "ArmLowerL", "ArmLowerR",
        "ArmUpperL", "ArmUpperR",
        "FootL", "FootR",
        "Head", "LegLowerL",
        "LegLowerR", "LegUpperL",
        "LegUpperR", "Neck",
        "PelvL", "PelvR",
        "PelvYL", "PelvYR",
        "ShoulderL", "ShoulderR"
    ]
    for name in motor_names:
        motors[name] = robot.getMotor(name)

    # Setters
    for motor in motors.values():
        motor.setPosition(0.0)
        motor.setVelocity(velocity)
        print("Resetting positions...")

async def everything():
    robot = Robot()
    await crouch(robot)
    #await wait(1)
    #await reach_out_and_grab(robot)
    #await wait(1)
    #await stand(robot)
    #await hands_behin_head(robot)
    #await throw(robot)
    #await wait(1)
    #await reset_positions(robot)

#main
if __name__ == "__main__":
    asyncio.run(everything())