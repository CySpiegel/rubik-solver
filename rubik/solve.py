import rubik.cube as rubik
import rubik.check as check


# if no rotate then default to front face clockwise rotate
def _solve(parms):
    result = {}
    stagedCubeString = ""
    validRotations = "FfRrBbLlUuDd"
    encodedCube = parms.get('cube',None)       #get "cube" parameter if present
    # result['solution'] = 'FfRrBbLlUuDd'        #example rotations
    # result['status'] = 'ok'               
    cubeToValidate = {}
    cubeToValidate['cube'] = encodedCube
    validateRotationMade = {}
    
    stagedCubeString =  encodedCube
    
    rotationList = parms.get('rotate', None)

    # Filter and validate encoded cubestring
    cubeToValidate = check._check(cubeToValidate)
    if cubeToValidate['status'] != 'ok':
        result['status'] = cubeToValidate['status']
    else:
        # If Rotation is empty or missing default to autosolving cube
        if (rotationList == None) or (rotationList == ''):
            # rotationList = 'F'
            rotationList = _autoSolveCube(stagedCubeString)
            result['solution'] = rotationList
            
            for move in rotationList:
                stagedCubeString = _applyMove(stagedCubeString, move)
                
            if _checkIfDownCrossIsSolved(stagedCubeString):
                result['status'] = 'ok'
            else:
                result['status'] = 'error: down cross not solved'
                
            if _isLowerLevelSolved(stagedCubeString):
                result['status'] = 'ok'
            else:
                result['status'] = 'error: lower level not solved'            
            
            if _isMiddleLayerSolved(stagedCubeString):
                result['status'] = 'ok'
            else:
                result['status'] = 'error: middle level not solved'

            return result
        else:
            # checks to see if the incoming given rotations are a string
            if (type(rotationList) == str):
                result['status'] = 'ok'
            else:
                result['status'] = "error: rotations is not a string"
            
            # turns the rotate into a list of actions or moves to be performed
            if result['status'] == 'ok': 
                rotationList = list(rotationList)
            
                # filter for valid moves in set of moves
                for move in rotationList:
                    if move in validRotations:
                        result['status'] = 'ok'
                    else:
                        result['status'] = 'error: invalid move detected'
                        break

            if result['status'] == 'ok':
                for move in rotationList:
                    stagedCubeString = _applyMove(stagedCubeString, move)
                    validateRotationMade['cube'] = stagedCubeString
                    validateRotationMade = check._check(validateRotationMade)
                    if validateRotationMade['status'] != 'ok':
                        result['status'] = validateRotationMade['status']
                        break

                result['cube'] = stagedCubeString
    return result


# Applies the given move aka action to the current cube string given
# returns modified cubestring from applied action or move



def _applyMove(cubeString, action):
    stagedCubeString = cubeString
    faceList = _parseCubeString(stagedCubeString)
    faceToRotate = _faceToRotate(action)
    stagedCubeString = _performRotation(faceList, faceToRotate, action)   
    return stagedCubeString

# break String into list of faces
# Returns the cube as a list of faces as strings
def _parseCubeString(cubeString):
    faceList = []
    
    frontFace = cubeString[0:9]
    rightFace = cubeString[9:18]
    backFace = cubeString[18:27]
    leftFace = cubeString[27:36]
    topFace = cubeString[36:45]
    bottomFace = cubeString[45:54]

    faceList.append(frontFace)
    faceList.append(rightFace)
    faceList.append(backFace)
    faceList.append(leftFace)
    faceList.append(topFace)
    faceList.append(bottomFace)
    
    return faceList


# Applies edge rotations pattern to the face of the cube being rotated
# determins what edges that need to be rotated with the selected facetorotate
# Returns the modified cube string with the applied edge rotations 
def _performRotation(listOfFaces, faceToRotate, direction):
    cubeString = ""
    rotatedFaceString = ""
    rotatedMatrixString = ""
    
    selectedFace = listOfFaces[faceToRotate]
    
    # Pre-Defined rotation pattern to rotate string
    # numbers are the face cells of the cube string index locations
    # that need to be swapped when the selected face rotates
    rightFaceClockwiseRotation = [(2, 38),(2,24),(2, 47),
                                  (5, 41), (5, 21), (5, 50),
                                  (8, 44),(8, 18),(8, 53)]
    
    rightFaceCounterClockwiseRotation = [(2, 47),(2,24),(2,38),
                                         (5, 50), (5, 21), (5, 41),
                                         (8, 53),(8, 18),(8, 44)]
    
    frontFaceClockwise = [(29, 44),(29, 15),(29,45),
                          (32, 43),(32, 12),(32, 46),
                          (35, 42),(35, 9),(35, 47)]
    
    frontFaceCounterClockwise = [(29, 45),(29, 15),(29,44),
                          (32, 46),(32, 12),(32, 43),
                          (35, 47),(35, 9),(35, 42)]
    
    backFaceClockwise = [(36, 33),(36, 53),(36, 11),
                         (37, 30),(37, 52),(37, 14),
                         (38, 27),(38, 51),(38, 17)]
    
    
    backFaceCounterClockwise = [(36, 11),(36, 53),(36, 33),
                                (37, 14),(37, 52),(37, 30),
                                (38, 17),(38, 51),(38, 27)]
    
    leftFaceClockwise = [(20, 42),(20, 6),(20, 51),
                         (23, 39),(23, 3),(23, 48),
                         (26, 36),(26, 0),(26, 45)]
    
    leftFaceCounterClockwise = [(20, 51),(20, 6),(20, 42),
                                (23, 48),(23, 3),(23, 39),
                                (26, 45),(26, 0),(26, 36)]
    
    upperFaceClockwise = [(27, 18),(27, 9),(27, 0),
                          (28, 19),(28, 10),(28, 1),
                          (29, 20),(29, 11),(29, 2)]

    upperFaceCounterClockwise = [(27, 0),(27, 9),(27, 18),
                                 (28, 1),(28, 10),(28, 19),
                                 (29, 2),(29, 11),(29, 20)]
    
    downFaceClockwise = [(35, 8),(35, 17),(35, 26),
                         (34, 7),(34, 16),(34, 25),
                         (33, 6),(33, 15),(33, 24)]
    
    downFaceCounterClockwise = [(35, 26),(35, 17),(35, 8),
                         (34, 25),(34, 16),(34, 7),
                         (33, 24),(33, 15),(33, 6)]
    
    
    # Return selected face as matrix
    faceMatrix = _faceToMatrix(selectedFace)
    
    # Rotate Selected Face Matrix based on direction
    rotatedMatrixString = _rotateMatrixFace(faceMatrix, direction)
    
    # Insert Rotated Matrix String back into list of faces
    listOfFaces[faceToRotate] = rotatedMatrixString
    
    # Turn list of Faces into cubeString
    cubeString = ''.join(listOfFaces)
    
    # Perform edge rotation on cube based on direction
    # need to consider jump list solution
    if direction == 'F':
        cubeString = _edgeRotate(cubeString, frontFaceClockwise)
    elif direction == 'f':
        cubeString = _edgeRotate(cubeString, frontFaceCounterClockwise)
    elif direction == 'R':
        cubeString = _edgeRotate(cubeString, rightFaceClockwiseRotation)
    elif direction == 'r':
        cubeString = _edgeRotate(cubeString, rightFaceCounterClockwiseRotation)
    elif direction == 'B':
        cubeString = _edgeRotate(cubeString, backFaceClockwise)
    elif direction == 'b':
        cubeString = _edgeRotate(cubeString, backFaceCounterClockwise)
    elif direction == 'L':
        cubeString = _edgeRotate(cubeString, leftFaceClockwise)
    elif direction == 'l':
        cubeString = _edgeRotate(cubeString, leftFaceCounterClockwise)
    elif direction == 'U':
        cubeString = _edgeRotate(cubeString, upperFaceClockwise)
    elif direction == 'u':
        cubeString = _edgeRotate(cubeString, upperFaceCounterClockwise)
    elif direction == 'D':
        cubeString = _edgeRotate(cubeString, downFaceClockwise)
    elif direction == 'd':
        cubeString = _edgeRotate(cubeString, downFaceCounterClockwise)
    elif direction == '':
        cubeString = _edgeRotate(cubeString, frontFaceClockwise)
    return cubeString

# Convert the incomming cube face string to a matrix
# Returns a the given face as a matrix
def _faceToMatrix(face):
    faceList = list(face)
    matrix = []
    matrix.append(faceList[0:3])  
    matrix.append(faceList[3:6])  
    matrix.append(faceList[6:9])  
    return matrix


# takes cubeString and roteates the edges based on the incoming patternSwapList
# returns rotated cubestring
def _edgeRotate(cubeString, patternSwapList):
    inputList = list(cubeString)
    for pair in patternSwapList:
        faceCellIndex, adjacentFaceCellIndex = pair
        inputList[faceCellIndex], inputList[adjacentFaceCellIndex] = inputList[adjacentFaceCellIndex], inputList[faceCellIndex]
    
    cubeStringEdgeRotated = ''.join(inputList)
    return cubeStringEdgeRotated


# Takes a cube face as a Matrix and rotates it based on direction
# returns the rotated face as matrix as a cube face string
def _rotateMatrixFace(facematrix, direction):
    rotatedFacematrix = []
    
    # if Direction is Upper Rotate Clockwise otherwise rotate counter clockwise
    if direction.isupper():
        rotatedFacematrix = _rotateMatrixClockwise(facematrix)
    else:
        rotatedFacematrix = _rotateMatrixCounterClockwise(facematrix)
        
    # flattens matrix back to string
    rotatedFaceString = ''.join(str(item) for innerlist in rotatedFacematrix for item in innerlist)
    return rotatedFaceString


# rotates a cubes face as a matrix clockwise
# returns a matrix
def _rotateMatrixClockwise(faceMatrix):
    rotatedMatrixClockwise = [[faceMatrix[row][col] for row in range(len(faceMatrix) -1,-1,-1)] for col in range(len(faceMatrix[0]))]
    return rotatedMatrixClockwise

# rotates a cubes face as a matrix counter clockwise
# returns matrix
def _rotateMatrixCounterClockwise(faceMatrix):
    rotatedMatrixCounterClockwise = [[faceMatrix[row][col] for row in range(len(faceMatrix))] for col in range(len(faceMatrix[0])-1,-1,-1)]
    return rotatedMatrixCounterClockwise


# AudoSolve Cube String is a Wrapper function and return list of moves needed to solve cube from 
# current cube state

def _autoSolveCube(cubeString):
    MovesToMake = ""
    solvedDaisyCube = ""
    # local copy of cubeString
    CubeCopy = cubeString
    
    #check if cube is already solved, if not solved then solve the daisy
    if _checkIfDownCrossIsSolved(cubeString) != True:
        MovesToMake, solvedDaisyCube = _solveForDaisyPetals(CubeCopy)
        DownCrossMoves, solvedDownCrossCube = _solveForDownCrossFromSolvedDaisy(solvedDaisyCube)
        MovesToMake = MovesToMake + DownCrossMoves
        CubeCopy = solvedDownCrossCube
    
    if _isLowerLevelSolved(CubeCopy) != True:
        MovesToMake, cubeWiteCornerOnTop = _moveWhitetInBottomCornerGroupsIfNotSolved(CubeCopy, MovesToMake)
        MovesToMake, LowerLevelSolved = _moveWhiteCornersFromTopToBottom(cubeWiteCornerOnTop, MovesToMake)
        
    if _isMiddleLayerSolved(CubeCopy) != True:
        MovesToMake, solvedMiddleLayer = _solveForMIddleLayer(CubeCopy, MovesToMake)

    return MovesToMake


def _solveForDaisyPetals(cubeString):
    MovesToMake = ""
    stagedCube = cubeString
    solvedDownCrossCube = ""
    white = stagedCube[49]
    daisyPetalIndex = { "Front": 43, "Right": 41 ,"Back": 37, "Left": 39 }
    
    while _checkIfDaisyIsSolved(stagedCube) == False:
        for side in daisyPetalIndex.keys():
            if stagedCube[daisyPetalIndex[side]] != white:
                
                # Check Edge for white
                actions = _findEdgeRotations(stagedCube, side)
                if actions != "":
                    MovesToMake = MovesToMake + actions
                else:
                    # Checking Matrix Face for White
                    actions = _findFaceRotations(stagedCube, side)
                    if actions != "":
                        MovesToMake = MovesToMake + actions
                    else:
                        MovesToMake = MovesToMake + "u"
                        actions = actions + 'u'
                
                for action in actions:
                    stagedCube = _applyMove(stagedCube, action)

    solvedDownCrossCube = stagedCube
    return MovesToMake, solvedDownCrossCube

def _solveForDownCrossFromSolvedDaisy(cubeString):
    MovesTomake = ""
    rotateCounterClockwise = "u"
    moveFrontPetalDown = "FF"
    moveRightPetalDown = "RR"
    moveBackPetalDown = "BB"
    moveLeftPetalDown = "LL"
    stagedCube = cubeString
    solvedDaisyCube = ""    
    
    # Get face Colors
    frontFaceColor = cubeString[4]
    rightFaceColor = cubeString[13]
    backFaceColor = cubeString[22]
    leftFaceColor = cubeString[31]
    
    bottomFaceColor = stagedCube[49]
    
    # Move Front Face Petal Down
    while True:
        if stagedCube[1] == frontFaceColor and stagedCube[43] == bottomFaceColor:
            MovesTomake = MovesTomake + moveFrontPetalDown
            for action in moveFrontPetalDown:
                stagedCube = _applyMove(stagedCube, action)

            break
        else:
            MovesTomake = MovesTomake + "u"
            stagedCube = _applyMove(stagedCube, rotateCounterClockwise)
            
            
    while True:
        if stagedCube[10] == rightFaceColor and stagedCube[41] == bottomFaceColor:
            MovesTomake = MovesTomake + moveRightPetalDown
            for action in moveRightPetalDown:
                stagedCube = _applyMove(stagedCube, action)        

            break
        else:
            MovesTomake = MovesTomake + "u"
            stagedCube = _applyMove(stagedCube, rotateCounterClockwise)
            
            
    while True:
        if stagedCube[19] == backFaceColor and stagedCube[37] == bottomFaceColor:
            MovesTomake = MovesTomake + moveBackPetalDown
            for action in moveBackPetalDown:
                stagedCube = _applyMove(stagedCube, action)        

            break
        else:
            MovesTomake = MovesTomake + "u"
            stagedCube = _applyMove(stagedCube, rotateCounterClockwise)
            

    while True:
        if stagedCube[28] == leftFaceColor and stagedCube[39] == bottomFaceColor:
            MovesTomake = MovesTomake + moveLeftPetalDown
            for action in moveLeftPetalDown:
                stagedCube = _applyMove(stagedCube, action)        

            break
        else:
            MovesTomake = MovesTomake + "u"
            stagedCube = _applyMove(stagedCube, rotateCounterClockwise)

    
    solvedDaisyCube =  stagedCube
    return MovesTomake, solvedDaisyCube





# Check if down cross is already solved and return True if its solved

def _checkIfDownCrossIsSolved(cubeString):
    #Get Face Colors
    isDownCrossSolved = False
    blue = cubeString[4]
    red = cubeString[13]
    green = cubeString[22]
    orange = cubeString[31]
    yellow = cubeString[40]
    white = cubeString[49]
    
    downCrossCellList = [46,48,50,52]
    
    whiteAdjacentBlue = cubeString[7]
    whiteAdjacentRed = cubeString[16]
    whiteAdjacentGreen = cubeString[25]
    whiteAdjacentOrange = cubeString[34]

    
    for index in downCrossCellList:
        if cubeString[index] != white:
            isDownCrossSolved = False
            return isDownCrossSolved
    
    if ((whiteAdjacentBlue == blue) and (whiteAdjacentRed == red) and
        (whiteAdjacentGreen == green) and 
        (whiteAdjacentOrange == orange)):
        isDownCrossSolved = True
    else:
        isDownCrossSolved = False
        
    return isDownCrossSolved
    
def _checkIfDaisyIsSolved(cubeString):
    isDaisyPetalsSolved = True
    # What Represents white
    white = cubeString[49]
    # Daisy cell index locations on top face
    daisyCellLocations = [37, 39, 41, 43]
    
    for index in daisyCellLocations:
        if cubeString[index] != white:
            isDaisyPetalsSolved = False      
    
    return isDaisyPetalsSolved


# Find the white cell for the given petal
# if found on edge return the moves to rotate it
# into possition on the selected petal
# if not found return empty string
def _findEdgeRotations(cubeString, selectedPetal):
    rotationsToMake = ""

    #Get color of white
    white = cubeString[49]
        
    if selectedPetal == "Front":
        if cubeString[12] == white:
            rotationsToMake = 'f'
            return rotationsToMake
        if cubeString[32] == white:
            rotationsToMake = 'F'
            return rotationsToMake
        if cubeString[46] == white:
            rotationsToMake = 'FF'
            return rotationsToMake
    
    if selectedPetal == "Left":
        if cubeString[3] == white:
            rotationsToMake = 'l'
            return rotationsToMake
        if cubeString[23] == white:
            rotationsToMake = 'L'
            return rotationsToMake
        if cubeString[48] == white:
            rotationsToMake = 'LL'
            return rotationsToMake
            
    if selectedPetal == "Right":
        if cubeString[21] == white:
            rotationsToMake = 'r'
            return rotationsToMake
        if cubeString[5] == white:
            rotationsToMake = 'R'
            return rotationsToMake
        if cubeString[50] == white:
            rotationsToMake = 'RR'
            return rotationsToMake
            
    if selectedPetal == "Back":
        if cubeString[30] == white:
            rotationsToMake = 'b'
            return rotationsToMake
        if cubeString[14] == white:
            rotationsToMake = 'B'
            return rotationsToMake
        if cubeString[52] == white:
            rotationsToMake = 'BB'
            return rotationsToMake
    
    return rotationsToMake
        

# find the rotations needed to get the daisy if white
# is found in the face of the adjacent side the petal is checking 
def _findFaceRotations(cubeString, selectedPetal):
    rotationsToMake = ""
    white = cubeString[49]
    
    if selectedPetal == "Front":
        if cubeString[1] == white:
            rotationsToMake = "FuRU"
            return rotationsToMake
        if cubeString[5] == white:
            rotationsToMake = "uRU"
            return rotationsToMake
        if cubeString[7] == white:
            rotationsToMake = "fuRU"
            return rotationsToMake
        if cubeString[3] == white:
            rotationsToMake = "Ulu"
            return rotationsToMake
            
    if selectedPetal == "Left":
        if cubeString[28] == white:
            rotationsToMake = "LuFU"
            return rotationsToMake
        if cubeString[32] == white:
            rotationsToMake = "uFU"
            return rotationsToMake
        if cubeString[34] == white:
            rotationsToMake = "luFU"
            return rotationsToMake
        if cubeString[30] == white:
            rotationsToMake = "Ubu"
            return rotationsToMake
            
    if selectedPetal == "Right":
        if cubeString[10] == white:
            rotationsToMake = "RuBU"
            return rotationsToMake
        if cubeString[14] == white:
            rotationsToMake = "uBU"
            return rotationsToMake
        if cubeString[16] == white:
            rotationsToMake = "ruBU"
            return rotationsToMake
        if cubeString[12] == white:
            rotationsToMake = "Ufu"
            return rotationsToMake
            
    if selectedPetal == "Back":
        if cubeString[19] == white:
            rotationsToMake = "BuLU"
            return rotationsToMake
        if cubeString[23] == white:
            rotationsToMake = "uLU"
            return rotationsToMake
        if cubeString[25] == white:
            rotationsToMake = "buLU"
            return rotationsToMake
        if cubeString[21] == white:
            rotationsToMake = "Uru"
            return rotationsToMake
            
    return rotationsToMake

def _isLowerLevelSolved(cubeString):
    isSolved = True
    frontFaceColor = cubeString[4]
    rightFaceColor = cubeString[13]
    backFaceColor = cubeString[22]
    leftFaceColor = cubeString[31]
    bottomFaceColor = cubeString[49]
    faceColorList = [frontFaceColor, rightFaceColor, backFaceColor, leftFaceColor]
    cubeSides = _parseCubeString(cubeString)
    
    sideOfFace = 0
    for selectedFaceColor in faceColorList:
        cubeFace = cubeSides[sideOfFace]
        bottomRowOfSelectedFace = cubeFace[6:9]
        for cellColor in bottomRowOfSelectedFace:
            if cellColor == selectedFaceColor:
                isSolved = True
            else:
                isSolved = False
                break
    
        if isSolved == False:
            break
        sideOfFace = sideOfFace + 1
    
    if isSolved == True:
        for cellColor in cubeSides[5]:
            if cellColor == bottomFaceColor:
                isSolved = True
            else:
                isSolved = False
                break
    return isSolved

def _triggerAction(cubeString, triggerDirection, selectedCubeFace, MovesToMake):
    triggerActions = {"RightTrigger": {"Front":"RUr", "Right":"BUb", "Back":"LUl", "Left":"FUf"},
                      "LeftTrigger": {"Front":"luL", "Right":"fuF", "Back":"ruR","Left":"buB"}}
    stagedCube = cubeString
    
    actions = triggerActions[triggerDirection][selectedCubeFace]
    MovesToMake = MovesToMake + actions
    for action in actions:
        stagedCube = _applyMove(stagedCube, action)
        
    return MovesToMake, stagedCube

def _isCornerSolved(cubeString, bottomCornerCell):
    isSolved = False
    stagedCube = cubeString
    
    frontFaceColor = cubeString[4]
    rightFaceColor = cubeString[13]
    backFaceColor = cubeString[22]
    leftFaceColor = cubeString[31]
    bottomFaceColor = cubeString[49]
    
    bottomCornerGroupings = {45: [45,35,6], 47:[47, 8, 15], 51:[51, 26, 33], 53:[51, 17, 24]}
    cornerGroupingColors = {45: [bottomFaceColor, leftFaceColor, frontFaceColor], 47: [bottomFaceColor, frontFaceColor, rightFaceColor], 
                            51:[bottomFaceColor, backFaceColor, leftFaceColor], 53:[bottomFaceColor, rightFaceColor,backFaceColor] }
    
    selectedCellGroup = bottomCornerGroupings[bottomCornerCell]
    expectedGroupColor = cornerGroupingColors[bottomCornerCell]
    
    groupIndex = 0
    for selectedCell in selectedCellGroup:
        if stagedCube[selectedCell] == expectedGroupColor[groupIndex]:
            isSolved = True
        else:
            isSolved = False
            break
        groupIndex = groupIndex + 1
            
    return isSolved

def _DetectWhiteCellsInCornerGroup(cubeString, cornerCell):
    isWhiteDetectedInGroup = False
    bottomFaceColor = cubeString[49]
    
    cornerGroupings = {45: [45,35,6], 47:[47, 8, 15], 51:[51, 26, 33], 53:[53, 17, 24], 
                       36:[36,20,27], 38:[38,11,18], 42:[42, 0, 29], 44:[44, 2, 9]}
    
    selectedGroupOfCells =  cornerGroupings[cornerCell]
    selectedGroupColors = []
    
    for cell in selectedGroupOfCells:
        selectedGroupColors.append(cubeString[cell])
        
    if bottomFaceColor in selectedGroupColors:
        isWhiteDetectedInGroup = True
    else:
        isWhiteDetectedInGroup = False

    return isWhiteDetectedInGroup

def _moveWhitetInBottomCornerGroupsIfNotSolved(cubeString, MovesToMake):
    stagedCube = cubeString
    triggerDirections = {45:"LeftTrigger", 47:"RightTrigger", 51:"RightTrigger", 53:"LeftTrigger"}
    selectedFace = {45:"Front", 47:"Front", 51:"Back", 53:"Back"}
    whiteAboveCornerCheck = {45:42, 47:44, 51:36, 53:38}
    cornersToCheck = [45, 47, 51, 53]
    
    cornersToMove = _makeListOfCornersToMove(stagedCube, cornersToCheck)

    for movingCornerToTop in cornersToMove:
        aboveCorner = whiteAboveCornerCheck[movingCornerToTop]
        MovesToMake, stagedCube = _findEmptyTopCorner(MovesToMake, stagedCube, aboveCorner)
        direction = triggerDirections[movingCornerToTop]
        selectedCubeFace = selectedFace[movingCornerToTop]
        MovesToMake, stagedCube = _triggerAction(stagedCube, direction, selectedCubeFace, MovesToMake)
            
    return MovesToMake, stagedCube

def _moveWhiteCornersFromTopToBottom(cubeString, MovesToMake):
    stagedCube = cubeString
    whiteColor = cubeString[49]
    
    cubeSide = {4:"Front", 13:"Right", 22:"Back", 31:"Left"}
    
    triggersFromFace = {"Front":{45:"LeftTrigger", 47:"RightTrigger"},
                        "Right":{47:"LeftTrigger", 53:"RightTrigger"},
                        "Back":{53:"LeftTrigger", 51:"RightTrigger"},
                        "Left":{51:"LeftTrigger", 45:"RightTrigger"}}
    
    specialCaseCorners = {45:"luuLUluL", 47:"RUUruRUr", 51:"LUUluLUl", 53:"ruuRUruR"}
    
    cornerToFaceMappings = {45:[31,4], 47:[4, 13], 51:[22, 31], 53:[13,22]}    
    aboveCorner = {45:42, 47:44, 51:36, 53:38}
    lowerCorners = [45, 47, 51, 53]
    faceToPerformTriggerFrom = None
    
    lowerCornersToSolve = _getListOfLowerCornersToSolve(stagedCube, lowerCorners)

    for selectedLowerCorner in lowerCornersToSolve:
        selectedTopCorner = aboveCorner[selectedLowerCorner]
        facesToSoveFrom = cornerToFaceMappings[selectedLowerCorner]
        
        stagedCube, MovesToMake = _rotateTopCornerToPossition(MovesToMake, stagedCube, selectedLowerCorner)
        
        topCornerColor = stagedCube[selectedTopCorner]
        if topCornerColor != whiteColor:
            for selectedFace in facesToSoveFrom:
                selectedFaceColor = stagedCube[selectedFace]
                if selectedFaceColor != topCornerColor:
                    faceToPerformTriggerFrom = cubeSide[selectedFace]
                    possibleTriggerActionsFromFace = triggersFromFace[faceToPerformTriggerFrom]
                    triggerDirection = possibleTriggerActionsFromFace[selectedLowerCorner]
                    MovesToMake, stagedCube = _triggerAction(stagedCube, triggerDirection, faceToPerformTriggerFrom, MovesToMake)
        else:
            actions = specialCaseCorners[selectedLowerCorner]
            for action in actions:
                MovesToMake = MovesToMake + action
                stagedCube = _applyMove(stagedCube, action)
            
    return MovesToMake, stagedCube

def _cornerColorsAboveMatchExpecetedBottomCornerColors(cubeString, bottomCornerCell):
    allColorsInGroup = False
    
    topCornerGroup = {36:[36,20,27], 38:[38,11,18], 42:[42, 0, 29], 44:[44, 2, 9]}
    
    associatedCornerOnTop = {45:42, 47:44, 51:36, 53:38}
    expectedCornerColorsForBottomCorner = {45: [cubeString[49],cubeString[4], cubeString[31]],
                                           47: [cubeString[49],cubeString[4], cubeString[13]],
                                           51: [cubeString[49],cubeString[22], cubeString[31]],
                                           53: [cubeString[49],cubeString[22], cubeString[13]]}
    
    expectedColors = expectedCornerColorsForBottomCorner[bottomCornerCell]
    assoceatedCorner = associatedCornerOnTop[bottomCornerCell]
    topCornerGroup = topCornerGroup[assoceatedCorner]
        
    for selectedCell in topCornerGroup:
        if cubeString[selectedCell] in expectedColors:
            allColorsInGroup = True
        else:
            allColorsInGroup = False
            break
    
    return allColorsInGroup

def _faceToRotate(action):
# Determin what face to orintate the model view from
    if action == 'F' or action == 'f':
        # Front face has been selected
        faceToRotate = 0
    elif action == 'R' or action == 'r':
        # Right face has been selected
        faceToRotate = 1
    elif action == 'B' or action == 'b':
        # Back Face has been selected
        faceToRotate = 2
    elif action == 'L' or action == 'l':
        # Left face has been selected
        faceToRotate = 3
    elif action == 'U' or action == 'u':
        faceToRotate = 4
    elif action == 'D' or action == 'd':
        faceToRotate = 5
    elif action == '':
        faceToRotate = 0
    return faceToRotate

def _makeListOfCornersToMove(stagedCube, cornersToCheck):
    cornersToMove = []
    for selectedCorner in cornersToCheck:
        if _DetectWhiteCellsInCornerGroup(stagedCube, selectedCorner):
            if _isCornerSolved(stagedCube, selectedCorner) == False:
                cornersToMove.append(selectedCorner)
    return cornersToMove

def _getListOfLowerCornersToSolve(stagedCube, lowerCorners):
    lowerCornersToSolve = []
    for selectedCorner in lowerCorners:
        if _DetectWhiteCellsInCornerGroup(stagedCube, selectedCorner):
            if _isCornerSolved(stagedCube, selectedCorner) == False:
                lowerCornersToSolve.append(selectedCorner)
        else:
            lowerCornersToSolve.append(selectedCorner)
    return lowerCornersToSolve

def _rotateTopCornerToPossition(MovesToMake, stagedCube, selectedLowerCorner):
    rotateTopFaceClockwise = "U"
    while _cornerColorsAboveMatchExpecetedBottomCornerColors(stagedCube, selectedLowerCorner) == False:
        MovesToMake = MovesToMake + rotateTopFaceClockwise
        stagedCube = _applyMove(stagedCube, rotateTopFaceClockwise)
    return stagedCube, MovesToMake

def _findEmptyTopCorner(MovesToMake, stagedCube, aboveCorner):
    rotateTopFaceClockwise = "U"
    while _DetectWhiteCellsInCornerGroup(stagedCube, aboveCorner):
        MovesToMake = MovesToMake + rotateTopFaceClockwise
        stagedCube = _applyMove(stagedCube, rotateTopFaceClockwise)
    return MovesToMake, stagedCube


def _isMiddleLayerSolved(cubeString):
    isMiddlelayerSoved = False
    blue = cubeString[4]
    red = cubeString[13]
    green = cubeString[22]
    orange = cubeString[31]
    faceColors = [blue, red, green, orange]
    edgepairsToCheck = {"Front": [3,5], "Right":[12,14], "Back": [21,23], "Left": [30,32]}
    
    count = 0
    for edge in edgepairsToCheck.values():
        if faceColors[count] != cubeString[edge[0]] or faceColors[count] != cubeString[edge[1]]:
            isMiddlelayerSoved = False
            break
        else:
            isMiddlelayerSoved = True
            count = count + 1
    return isMiddlelayerSoved


def _isYellowInTopEdge(cubeString):
    yellowInTopPedal = True
    yellow = cubeString[40]
    cubeCellList = [[cubeString[1],cubeString[43]],[cubeString[10],cubeString[41]],
                    [cubeString[19],cubeString[37]],[cubeString[28],cubeString[39]]]
    
    for cell in cubeCellList:
        if yellow not in cell:
            yellowInTopPedal = False
            break

    return yellowInTopPedal


def _moveEdgeToMatchingFaceColor(cubeString, edgeColor, faceColorList, MovesToMake):
    stagedCube = cubeString
    rotateDirection = 'u'
    for faceColor in faceColorList:
        if edgeColor == faceColor:
            break
        else:
            MovesToMake = MovesToMake + rotateDirection
            stagedCube = _applyMove(stagedCube, rotateDirection)
    
    return stagedCube, MovesToMake


def _moveTopEdgeToSolvedPossition(cubeString, edgePair, faceColorList, MovesToMake):
    stagedCube = cubeString
    rotationToMake = ''
    faceColorToTheRight = faceColorList[2]
    faceColorToTheLeft = faceColorList[4]
    selectedFace = faceColorList[0]
    
    selectedTopCell = edgePair[1]
    
    if selectedTopCell == faceColorToTheRight:
        rotationToMake, MovesToMake, stagedCube = _performRightEdgeToSolvePossition(MovesToMake, stagedCube, rotationToMake, selectedFace)
        
    elif selectedTopCell == faceColorToTheLeft:
        stagedCube, MovesToMake = _performLeftEdgeToSolvePossition(MovesToMake, stagedCube, rotationToMake, selectedFace)
        
    return stagedCube, MovesToMake


def _solveForMIddleLayer(cubeString, MovesToMake):
    stagedCube = cubeString
    blue = cubeString[4]
    red = cubeString[13]
    green = cubeString[22]
    orange = cubeString[31]
    yellow = cubeString[40]
    
    performSpecialCaseTrigger = {"LeftTrigger": {"Front":[3, blue], "Right":[12, red], "Back":[21, green],"Left":[30, orange]},
                                 "RightTrigger": {"Front":[5, blue], "Right":[14, red], "Back":[23, green], "Left":[32, orange]}}
    
    faceSearchDirections = {"Front": [["Front", blue, red, green, orange], [1,43]],
                            "Right": [["Right", red, green, orange, blue], [10,41]],
                            "Back": [["Back", green, orange, blue, red], [19, 37]],
                            "Left": [["Left", orange, blue, red, green], [28, 39]]}
    
    while(_isMiddleLayerSolved(stagedCube) == False):        
        if (_isYellowInTopEdge(stagedCube) == True):
            stagedCube, MovesToMake = _performTriggers(MovesToMake, stagedCube, performSpecialCaseTrigger)

        MovesToMake, stagedCube = _performFaceSearch(MovesToMake, stagedCube, yellow, faceSearchDirections)

    return MovesToMake, stagedCube



def _performTriggers(MovesToMake, stagedCube, performSpecialCaseTrigger):
    for triggerType in performSpecialCaseTrigger:
        for selectedFace in performSpecialCaseTrigger[triggerType]:
            edgeFacePair = performSpecialCaseTrigger[triggerType][selectedFace]
            cellIndex = edgeFacePair[0]
            faceColor = edgeFacePair[1]
            if stagedCube[cellIndex] != faceColor:
                MovesToMake, stagedCube = _triggerAction(stagedCube, triggerType, selectedFace, MovesToMake)
                MovesToMake, stagedCube = _moveWhiteCornersFromTopToBottom(stagedCube, MovesToMake)
                break
            
    return stagedCube, MovesToMake


def _performFaceSearch(MovesToMake, stagedCube, yellow, faceSearchDirections):
    for searchDirection in faceSearchDirections:
        selectedFaceSearchPattern = faceSearchDirections[searchDirection][0]
        edgePairCellIndacies = faceSearchDirections[searchDirection][1]
        edgePairColors = [stagedCube[edgePairCellIndacies[0]], stagedCube[edgePairCellIndacies[1]]]
        if yellow not in edgePairColors:
            selectedFaceColor = selectedFaceSearchPattern[1]
            stagedCube, MovesToMake = _moveEdgeToMatchingFaceColor(stagedCube, edgePairColors[0], selectedFaceSearchPattern[1:], MovesToMake)
            if edgePairColors[0] == selectedFaceColor:
                stagedCube, MovesToMake = _moveTopEdgeToSolvedPossition(stagedCube, edgePairColors, selectedFaceSearchPattern, MovesToMake)
    
    return MovesToMake, stagedCube


def _performRightEdgeToSolvePossition(MovesToMake, stagedCube, rotationToMake, selectedFace):
    rotationToMake = "U"
    MovesToMake = MovesToMake + rotationToMake
    stagedCube = _applyMove(stagedCube, rotationToMake)
    MovesToMake, stagedCube = _triggerAction(stagedCube, "RightTrigger", selectedFace, MovesToMake)
    MovesToMake, stagedCube = _moveWhiteCornersFromTopToBottom(stagedCube, MovesToMake)
    return rotationToMake, MovesToMake, stagedCube


def _performLeftEdgeToSolvePossition(MovesToMake, stagedCube, rotationToMake, selectedFace):
    rotationToMake = "u"
    MovesToMake = MovesToMake + rotationToMake
    stagedCube = _applyMove(stagedCube, rotationToMake)
    MovesToMake, stagedCube = _triggerAction(stagedCube, "LeftTrigger", selectedFace, MovesToMake)
    MovesToMake, stagedCube = _moveWhiteCornersFromTopToBottom(stagedCube, MovesToMake)
    return stagedCube, MovesToMake














