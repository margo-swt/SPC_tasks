# SPC_tasks

mock server task can be found on separate branch , in case you have faced issues with file

### appium automation task

The goal of this test is to log in to the space bank , update passcode and check it

#### run requirements.txt before test_execution

### Notice 
#### python version 3.10.2
> For user you should provide a test user credentials and place them in terminal  , you will see a couple of methods like this. They were created in order to avoid static datas in code, because OTP interactions

```Python
    def test_member_mobile(self):
        test_user_spc = test_mobile_mock_user_spc.mobile_test_user()
        with assume: assert test_user_spc.is_displayed() == True
        with assume: assert test_user_spc.is_enabled() == True
        test_mobile = str(input('⚠️Enter test number: '))
        test_user_spc.send_keys(test_mobile)
```

you can run test with command
```commandline
pytest
```

The second task about mocks - in case there were issues in attachment, view it on branch

```commandline
spc_mock_server
```

