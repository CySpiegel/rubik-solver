import unittest
import rubik.solve as solve



class Test(unittest.TestCase):

# analysis:    solve
#
#
#    inputs:    
#        parms:           dictionary; mandatory, arrives validates
#        parms['op]       string, "solve"; mandatory; arrives validated
#        parms['cube']    string; length = 54, [azAZ09], ...; mandatory, arrives unvalidated
#        parms['rotate']  string: len >= 0; [FfRrBbLlUuDd]; optional, defaul to F is missing; arrives unvalidated
#
#    outputs:
#        side-effects: no state change; no external effects
#        returns: dictionary
#            nominal:
#                dictionary['cube]: string, len=54
#                dictionary['status']: 'ok'
#            abnormal:
#                dictoinary['status']: 'error: xxx'
#
#    happy path
#        test 010: normal valid cube with F rotation
#        test 020: normal valid cube with f rotation
#        test 030: normal valid cube with R rotation
#        test 040: normal valid cube with r rotation
#        test 050: normal valid cube with B rotation
#        test 060: normal valid cube with b rotation
#        test 070: normal valid cube with L rotation
#        test 080: normal valid cube with l rotation
#        test 090: normal valid cube with U rotation
#        test 011: normal valid cube with u rotation
#        test 012: normal valid cube with D rotation
#        test 013: normal valid cube with d rotation

#        test 014: normal valid cube with "" rotation

#    sad path
#        test 910: missing cube
#        test 920: normal valid cube, invalid rotation

    
    # def test_solve_010_ShouldRotatevalidNominalCubeF(self):
    #     inputDict = {}
    #     inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
    #     inputDict['rotate'] = 'F'
    #     inputDict['op'] = 'solve'
    #
    #     expectedResult = {}
    #     expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
    #     expectedResult['status'] = 'ok'
    #
    #     actualResult = solve._solve(inputDict)
    #
    #     self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    #     self.assertEqual(expectedResult.get('status'), actualResult.get('status')
    
        # Rotate Front Face Clockwise
        def test_solve_010_ShouldRotatevalidNominalCubeF(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'F'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbyrryrryrrgggggggggoowoowoowyyyyyyooorrrwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        # Rotate front face counter clockwise
        def test_solve_020_ShouldRotatevalidNominalCubef(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbyrryrryrrgggggggggoowoowoowyyyyyyooorrrwwwwww'
            inputDict['rotate'] = 'f'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    # Rotate Right face Clockwise
        def test_solve_030_ShouldRotatevalidNominalCubeR(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'R'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbwbbwbbwrrrrrrrrryggyggyggoooooooooyybyybyybwwgwwgwwg'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
         
        # Rotate the cube counter clockwise   
        def test_solve_040_ShouldRotatevalidNominalCuber(self):
            inputDict = {}
            inputDict['cube'] = 'bbwbbwbbwrrrrrrrrryggyggyggoooooooooyybyybyybwwgwwgwwg'
            inputDict['rotate'] = 'r'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
            # Rotate front face counter clockwise
        def test_solve_050_ShouldRotatevalidNominalCubeB(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'B'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrwrrwrrwgggggggggyooyooyoorrryyyyyywwwwwwooo'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        # Rotate back face counter clockwise
        def test_solve_060_ShouldRotatevalidNominalCubeb(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrwrrwrrwgggggggggyooyooyoorrryyyyyywwwwwwooo'
            inputDict['rotate'] = 'b'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        # Rotate left face clockwise
        def test_solve_070_ShouldRotatevalidNominalCubeL(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'L'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'ybbybbybbrrrrrrrrrggwggwggwooooooooogyygyygyybwwbwwbww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        # Rotate left face Counter Clockwise
        def test_solve_080_ShouldRotatevalidNominalCubel(self):
            inputDict = {}
            inputDict['cube'] = 'ybbybbybbrrrrrrrrrggwggwggwooooooooogyygyygyybwwbwwbww'
            inputDict['rotate'] = 'l'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    

        # Rotate Upwards face Clockwise
        def test_solve_090_ShouldRotatevalidNominalCubeU(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'U'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'rrrbbbbbbgggrrrrrroooggggggbbbooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            

        # Rotate Upwards face Counter Clockwise
        def test_solve_011_ShouldRotatevalidNominalCubeu(self):
            inputDict = {}
            inputDict['cube'] = 'rrrbbbbbbgggrrrrrroooggggggbbbooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'u'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            

        # Rotate Downword face Clockwise
        def test_solve_012_ShouldRotatevalidNominalCubeD(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'D'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbooorrrrrrbbbggggggrrroooooogggyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        # Rotate Downword face Counter Clockwise
        def test_solve_013_ShouldRotatevalidNominalCubed(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbooorrrrrrbbbggggggrrroooooogggyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'd'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        # Rotate Rotation mission default to front face Clockwise
        def test_solve_014_ShouldRotatevalidNominalCubeRotateMissing(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = ''
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbyrryrryrrgggggggggoowoowoowyyyyyyooorrrwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        def test_solve_015_ShouldRotatevalidNominalCubeRotateMissingFromDictionary(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            # inputDict['rotate'] = ''
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbyrryrryrrgggggggggoowoowoowyyyyyyooorrrwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
            
        # Rotate Front Face 4 time in a row of solved cube, should return solved cube 
        def test_solve_016_ShouldRotatevalidNominalCubeRotateF4Times(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'FFFF'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        # Rotate Right Face 4 time in a row of solved cube, should return solved cube 
        def test_solve_017_ShouldRotatevalidNominalCubeRotateR4Times(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'RRRR'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        def test_check_018_SolveScamboledCube(self):
            inputDict = {}
            inputDict['cube'] = 'rbbgbobbgrgwyrywyobggrggywgoryyowowwyoobyrgwyrorrwbwob'
            inputDict['rotate'] = 'FLFFBUUdLfDrFLdRRdLLdRRu'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
        
            actualResult = solve._solve(inputDict)
        
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        # Sad Path testing
            
        # Rotate Right Face 4 time in a row of solved cube, should return solved cube 
        def test_solve_029_ShouldThrowErrorOnInvalidMove(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'W'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['status'] = 'error: invalid move detected'
            expectedDictLength = 1
        
            actualResult = solve._solve(inputDict)
            actualDictLength = len(actualResult.keys())
        
            self.assertEqual(expectedDictLength, actualDictLength)
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
            
        def test_solve_030_ShouldThrowErrorOnInvalidMoveInListOfRotations(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'RRRLLLBbBEEUud'
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['status'] = 'error: invalid move detected'
            expectedDictLength = 1
        
            actualResult = solve._solve(inputDict)
            actualDictLength = len(actualResult.keys())
        
            self.assertEqual(expectedDictLength, actualDictLength)
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        # Invalid cube shoudl return just error     
        def test_check_031_FailOnCubeStringContainedIllegalCharacter(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrggggggggg@@@@@@@@@yyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'RRRLLLBbBUud'
            inputDict['op'] = 'solve'
            
            
            expectedResult = {}
            expectedResult['status'] = 'error: cube string contains non-valid colors'
            expectedDictLength = 1
        
            actualResult = solve._solve(inputDict)
            
            actualDictLength = len(actualResult.keys())
        
        
            self.assertEqual(expectedDictLength, actualDictLength)
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

          
        # Cube Missing from dictionary, return error     
        def test_check_032_CubeMissingFronDictionary(self):
            inputDict = {}
            inputDict['rotate'] = 'RRRLLLBbBUud'
            inputDict['op'] = 'solve'
            
            
            expectedResult = {}
            expectedResult['status'] = 'error: cube not exist in dictionary'
            expectedDictLength = 1
        
            actualResult = solve._solve(inputDict)
            
            actualDictLength = len(actualResult.keys())
        
        
            self.assertEqual(expectedDictLength, actualDictLength)
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
            
        # Cube Missing from dictionary, return error     
        def test_check_032_InputDictionaryMissingCubeAndRotate(self):
            inputDict = {}
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['status'] = 'error: cube not exist in dictionary'
            expectedDictLength = 1
        
            actualResult = solve._solve(inputDict)
            
            actualDictLength = len(actualResult.keys())
        
        
            self.assertEqual(expectedDictLength, actualDictLength)
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
            
        def test_solve_033_FailOnRotationsAsList(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = ['R','R','R','L','L','L','B','b','B','U','u','d']
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['status'] = 'error: rotations is not a string'
            expectedDictLength = 1
        
            actualResult = solve._solve(inputDict)
            actualDictLength = len(actualResult.keys())
        
            self.assertEqual(expectedDictLength, actualDictLength)
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_solve_034_ShouldThrowErrorOnSpaceAsRotation(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = ' '
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['status'] = 'error: invalid move detected'
            expectedDictLength = 1
        
            actualResult = solve._solve(inputDict)
            actualDictLength = len(actualResult.keys())
        
            self.assertEqual(expectedDictLength, actualDictLength)
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_solve_034_ShouldThrowErrorOnRotationAsNumbers(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 123
            inputDict['op'] = 'solve'
        
            expectedResult = {}
            expectedResult['status'] = 'error: rotations is not a string'
            expectedDictLength = 1
        
            actualResult = solve._solve(inputDict)
            actualDictLength = len(actualResult.keys())
        
            self.assertEqual(expectedDictLength, actualDictLength)
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))