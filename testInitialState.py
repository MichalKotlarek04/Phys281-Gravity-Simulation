from initialState import getBodyState

earthState = getBodyState("earth").initial_state
earthPosVec = earthState[0]
earthVelVec = earthState[1]
print(earthPosVec)
print(earthVelVec)
    
