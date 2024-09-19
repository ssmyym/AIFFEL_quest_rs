# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 윤철희 
- 리뷰어 : 최세영


# PRT(Peer Review Template)
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
        - 중요! 해당 조건을 만족하는 부분을 캡쳐해 근거로 첨부
        - ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c09f8228-29c7-4dcb-8ca3-1de7d3988fab/8a3b4463-605b-4036-a0f9-ec2b540920c7/image.png)
        - ![image](https://github.com/user-attachments/assets/3de32bd0-f716-46a6-affd-b93b5fc0ec2b)
        - ![image](https://github.com/user-attachments/assets/2dbde816-bf40-41a6-b02a-ac9bf52584c7)
        - ![image](https://github.com/user-attachments/assets/6f8db197-d4c7-4498-a17a-67cb18cfb927)
        - **총 3개의 모델**을 가져오셨으나, 아쉽게도 메모리 문제와 해결되지 못한 에러들 때문에 학습이 완료되지는 못했습니다.



- [O]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 해당 코드 블럭을 왜 핵심적이라고 생각하는지 확인
    - 해당 코드 블럭에 doc string/annotation이 달려 있는지 확인
    - 해당 코드의 기능, 존재 이유, 작동 원리 등을 기술했는지 확인
    - 주석을 보고 코드 이해가 잘 되었는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        - ![image](https://github.com/user-attachments/assets/3de32bd0-f716-46a6-affd-b93b5fc0ec2b)
        - ![image](https://github.com/user-attachments/assets/2dbde816-bf40-41a6-b02a-ac9bf52584c7)
        - ![image](https://github.com/user-attachments/assets/6f8db197-d4c7-4498-a17a-67cb18cfb927)
        - **주석이나 doc string**을 모델을 가져오는 부분에서 특히 많이 보게 되었는데, 각각의 코드에 대해 어떤 레이어를 정의한 것인지 설명이 잘 나와있었습니다.
        
- [O]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 문제 원인 및 해결 과정을 잘 기록하였는지 확인
    - 프로젝트 평가 기준에 더해 추가적으로 수행한 나만의 시도, 
    실험이 기록되어 있는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        - ![image](https://github.com/user-attachments/assets/79dfdc39-d167-4bbc-bf83-55fce2fa6614)
        - ![image](https://github.com/user-attachments/assets/f5a81a8f-76e0-4e70-8b47-d2463eee8b05)
        - ![image](https://github.com/user-attachments/assets/13f3bdfb-721b-46ac-959f-d42ca63cdce7)
        - 총 3개의 에러를 확인할 수 있는데, 해결되지 못한 에러가 아쉽게도 존재했습니다. 하지만, simple RNN 모델에 나타난 에러를 해결하여 결과를 보여주셨습니다
        - ![image](https://github.com/user-attachments/assets/caecc413-5cfe-409d-bb86-4a8248430e48)




        
- [O]  **4. 회고를 잘 작성했나요?**
    - 주어진 문제를 해결하는 완성된 코드 내지 프로젝트 결과물에 대해
    배운점과 아쉬운점, 느낀점 등이 기록되어 있는지 확인
    - 전체 코드 실행 플로우를 그래프로 그려서 이해를 돕고 있는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        - ![image](https://github.com/user-attachments/assets/f4c4bcbf-87e2-423a-8078-95399b2cde27)
        - 적절하게 회고를 잘 작성해주셨습니다. 아쉽게 전처리 부분에서 에러가 많이 나시고, 해결이 잘 안된 부분이 많아서 실험을 진행하기 어려우셨던 것 같습니다.

        
- [O]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화/모듈화했는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        - ![image](https://github.com/user-attachments/assets/1e0c964e-6f8e-43e0-9ab5-6804ea09d22d)
        - 이렇게 초반에 필요한 모듈을 import 해주고,
        - ![image](https://github.com/user-attachments/assets/ca683dff-f244-4243-a37c-e419f84d0bd9)
        - 중복을 방지하기 위해 함수화를 적극활용하였습니다.




# 회고(참고 링크 및 코드 개선)
```
철희님은 어떤 모델을 활용할지에 대한 경험치와 실험 조건에서 모델의 차이에 따른 성능 변화만을 관찰하기 위해, layer의 구성을 최대한 비슷하게 한다거나, unit 수를 고정하는 등 제가 생각하기에는 어려운 조건들을 잘 설정하시는 것 같습니다.
아쉽게도 해결되지 못한 에러들 때문에, 최종적인 결과를 보여주시진 못하셨지만, 고생하신 흔적을 많이 보게 된 것 같습니다!
고생하셨습니다!
```
