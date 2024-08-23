# ROS-python-topic
ROS turtorials for study
>**Note:**
>* ROS 사용에 익숙해 지기 위해 간단한 코드를 만들어 업로드하게되었습니다.
>* python을 사용하여 topic을 publisher와 subscriber를 생성하였습니다.
실행방법은 다음과 같다

## Overview

![python_topic](https://github.com/user-attachments/assets/04cc302a-f42e-4b7a-a183-2ed157b76e49)

## Dependencies

[python3](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu) 를 사용하며 운영 체제는 Ubuntu이다.

## Getting Started
### 1. Clone

이 repository를 clone 한다.
([How to "git clone" including submodules?](https://stackoverflow.com/questions/3796927/how-to-git-clone-including-submodules))

```sh
cd .
mkdir ROS-python-topic
cd ROS-python-topic
git clone https://github.com/shj96227/ROS-python-topic.git
```

### 2. Run Publisher & Subscriber

```sh
roscore
rosrun my_first_python talker.py
rosrun my_first_python listener.py
```

