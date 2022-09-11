import rubik.cube as rubik

def _check(parms):
    result = {}
    encodedCube = parms.get('cube',None)
    
    result = _doesCubeExist(encodedCube)
    
    if 'ok' in result.values():
        result = _isEncodedCubeAString(encodedCube)
        
    if 'ok' in result.values():
        result = _lengthOfCubeStringCorrect(encodedCube)
        
    if 'ok' in result.values():
        result = _isAlphaNumericString(encodedCube)
    

    if 'ok' in result.values():
        result = _countColorsOfFaces(encodedCube)
        
    if 'ok' in result.values():
        result = _areCenterFaceColorsUnique(encodedCube)
    
    if 'ok' in result.values():
        result = _checkCornerAdjasentColorsPossible(encodedCube)
        
    if 'ok' in result.values():
        result = _checkNoneCornerAdjasentColorsPossible(encodedCube)

    return result

# Check if key of cube even exists in rubix cube parms
def _doesCubeExist(parms):
    result = {}
    message = ''
    
    if parms != None:
        message = 'ok'
    else:
        message = 'error: cube not exist in dictionary'
        
    result['status'] = message
    return result

def _isEncodedCubeAString(encodedCube):
    result = {}
    message = ''
    if (type(encodedCube) == str):
        message = 'ok'
    else:
        message = 'error: encodedCube not a string'
    
    result['status'] = message
    return result

# Check Length of Cube String must be 54 character
def _lengthOfCubeStringCorrect(encodedCube):
    expectedLength = 54
    result = {}
    message = '_lengthOfCubeStringCorrect'
    
    actualLength = len(encodedCube)
    if(actualLength == expectedLength):
        message = 'ok'
    else:
        message = 'error: cube string length is not 54 its ' + str(actualLength)
    
    result['status'] = message
    return result


# Check validity of cube string only contains [a-zA-Z0-9]
def _isAlphaNumericString(encodedCube):
    result = {}
    message = '_isAlphaNumericString'
    for character in encodedCube:
        if (character.isalpha() or character.isnumeric()):
            message = 'ok'
        else:
            message = 'error: cube string contains non-valid colors'
            break
    
    result['status'] = message
    return result

# Count the total number of colors that belong to each color
# There should be a total of 6 unique colors each with a count
# of 9 faces
def _countColorsOfFaces(encodedCube):
    result = {}
    colorCount = {}
    message = '_countColorsOfFaces'
    
    for index, character in enumerate(encodedCube):
        if (character in colorCount):
            colorCount[character] += 1
        else:
            colorCount[character] = 1
    
    # check for correct number of colors
    if (len(colorCount) == 6): 
        for key, count in colorCount.items():
            if count == 9:
                message = 'ok'
            else:
                message = 'error: color ' + key + ' count is not 9'
                break
    else:
        message = 'error: number of unique colors is not 6'
    
    result['status'] = message
    return result

# check that at each center of each face is a unique color
# index positions to check  4, 14, 22, 31, 40, 49
def _areCenterFaceColorsUnique(encodedCube):
    result = {}
    centerFaceLocation = [4, 13, 22, 31, 40, 49]
    faceColors = {}
    message = '_areCenterFaceColorsUnique'
    
    for index in centerFaceLocation:
        color = encodedCube[index]
        if color not in faceColors:
            faceColors[color] = 1
            message = 'ok'
        else:
            message = 'error: duplicate colors at cube center of face index ' + str(index)
            break
        
    result['status'] = message
    return result

# 
def _checkCornerAdjasentColorsPossible(encodedCube):
    result = {}
    centerFaceLocation = [4, 13, 22, 31, 40, 49]
    cubeSide = ['Front', 'Right', 'Back', 'Left', 'Top', 'Bottom']
    
    cubeCornerSets = [[ 0, 29, 42], 
                      [ 2, 9, 44],
                      [ 8, 15, 47],
                      [ 6, 45, 35],
                      [ 36, 20, 27],
                      [ 38, 11, 18],
                      [ 17, 24, 53],
                      [ 51, 33, 26]]
    
    # get list of center colors and what face it belongs to
    # assign to side
    # 0 = Front
    # 1 = Right
    # 2 = Back
    # 3 = Left
    # 4 = Top
    # 5 = Bottom
    # centerFaceColors = []
    # for index in centerFaceLocation:
    #     color = encodedCube[index]
    #     centerFaceColors.append(color)
    #     print(cubeSide[centerFaceLocation.index(index)], color)
    
    frontColor = encodedCube[centerFaceLocation[0]]
    rightColor = encodedCube[centerFaceLocation[1]]
    backColor = encodedCube[centerFaceLocation[2]]
    leftColor = encodedCube[centerFaceLocation[3]]
    topColor = encodedCube[centerFaceLocation[4]]
    bottomColor = encodedCube[centerFaceLocation[5]]
    
    message = 'ok'
    listOfColorsInCornerSet = []
    impossibleSets = [[frontColor, backColor], [leftColor, rightColor], [topColor, bottomColor]]
    # Check all corners to see if there exist a corner thats impossible
    # Check Oposing Sides sets
    for impossibleColorSet in impossibleSets:
        primary = impossibleColorSet[0]
        secondary = impossibleColorSet[1] 

        # Check if opposing colors are in a corner set
        # its impossible for both primary and secondary to be in the same corner set
        for currentCornerSet in cubeCornerSets:
            for index in currentCornerSet:
                listOfColorsInCornerSet.append(encodedCube[index])
                

            if primary in listOfColorsInCornerSet and secondary in listOfColorsInCornerSet:
                message = 'error: impossible color positions in corners'
                listOfColorsInCornerSet = []                
                break
            
            listOfColorsInCornerSet = []



    result['status'] = message
    return result

def _checkNoneCornerAdjasentColorsPossible(encodedCube):
    result = {}
    centerFaceLocation = [4, 13, 22, 31, 40, 49]    
    cubeCornerSets = [[ 1, 43 ], 
                      [ 7, 46 ],
                      [ 3, 32],
                      [ 5, 12],
                      [ 37, 19],
                      [ 14, 21],
                      [ 30, 23],
                      [ 52, 25],
                      [ 41, 10],
                      [ 39, 28],
                      [ 16, 50],
                      [ 48, 34]]
    
    # get list of center colors and what face it belongs to
    # assign to side
    # 0 = Front
    # 1 = Right
    # 2 = Back
    # 3 = Left
    # 4 = Top
    # 5 = Bottom
    # centerFaceColors = []
    # for index in centerFaceLocation:
    #     color = encodedCube[index]
    #     centerFaceColors.append(color)
    #     print(cubeSide[centerFaceLocation.index(index)], color)
    
    frontColor = encodedCube[centerFaceLocation[0]]
    rightColor = encodedCube[centerFaceLocation[1]]
    backColor = encodedCube[centerFaceLocation[2]]
    leftColor = encodedCube[centerFaceLocation[3]]
    topColor = encodedCube[centerFaceLocation[4]]
    bottomColor = encodedCube[centerFaceLocation[5]]
    
    message = 'ok'
    listOfColorsInCornerSet = []
    impossibleSets = [[frontColor, backColor], [leftColor, rightColor], [topColor, bottomColor]]
    # Check all corners to see if there exist a corner thats impossible
    # Check Oposing Sides sets
    for impossibleColorSet in impossibleSets:
        primary = impossibleColorSet[0]
        secondary = impossibleColorSet[1] 

        # Check if opposing colors are in a corner set
        # its impossible for both primary and secondary to be in the same corner set
        for currentCornerSet in cubeCornerSets:
            for index in currentCornerSet:
                listOfColorsInCornerSet.append(encodedCube[index])
                

            if primary in listOfColorsInCornerSet and secondary in listOfColorsInCornerSet:
                message = 'error: impossible color positions in sides'
                listOfColorsInCornerSet = []                
                break
            
            listOfColorsInCornerSet = []
 
    result['status'] = message
    return result
    

