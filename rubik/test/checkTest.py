from unittest import TestCase
import rubik.check as check 


class CheckTest(TestCase):
    
    # # Happy path
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
        
    def test_check_020_ShouldReturnOkOnSolvedCubeWithLettersAndNumbers(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbb111111111gggggggggooooooooo999999999wwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    
    def test_check_030_ShouldReturnOkOnSolvedCubeOnlyLetters(self):
        parm = {'op':'check',
                'cube':'111111111222222222333333333444444444555555555666666666'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')


    def test_check_040_ShouldReturnOkScrambledCube(self):
        parm = {'op':'check',
                'cube':'ywbbbywryyobrowowrwgbggogrgrwgyrooybyyrowgrroobgbybwgw'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
        
        

    # # Sad path
    def test_check_110_FailOnEmptyString(self):
        parm = {'op':'check',
                'cube': ''}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    def test_check_111_FailOnCubeStringNotHaving9FacesInAColor(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggooooooooooyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    def test_check_120_FailWhenCubeStringIsNumbers(self):
        parm = {'op':'check',
                'cube': 111111111222222222333333333444444444555555555666666666}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    def test_check_130_FailOnCubeStringIsNone(self):
        parm = {'op':'check',
                'cube': None}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    def test_check_140_FailOnCubeIsNestedDictionary(self):
        parm = {'op':'check',
                'cube': {'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    
    def test_check_150_FailOnCubeStringIsToShort(self):
        parm = {'op':'check',
                 'cube': 'bbbbbbbbb'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_151_FailOnCubeStringIsToLong(self):
        parm = {'op':'check',
                 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwwwwwwwwwwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    
    def test_check_160_FailOnCubeStringAllSameColor(self):
        parm = {'op':'check',
                 'cube': 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_170_FailOnCubeCenterFacePositionNotUnique(self):
        parm = {'op':'check',
                'cube': 'bbbbwbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwbw'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    def test_check_180_FailOnCubeNotInDictionary(self):
        parm = {'op':'check'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_190_FailOnCubeStringContainedIllegalCharacter(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrggggggggg@@@@@@@@@yyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    # # Happy path
    def test_check_1100_FailOnCubeNotSolvableCornerCombination(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbgrrrrrrrrrggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_1101_FailOnCubeNotSolvableEdgeCombination(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggygoooooooooygyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    


