# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 윤철희
- 리뷰어 : 홍사


# PRT(Peer Review Template)
- [O]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - ![image](https://github.com/user-attachments/assets/e0fd2f0c-fa5c-4edd-ba56-8b3e92eac3d0)
    - CAM 모델 그래프
    - ![image](https://github.com/user-attachments/assets/e300e2b5-6e92-4b88-92e7-bce2bb4b5be5)
    - CAM 사진
    - ![image](https://github.com/user-attachments/assets/0ef709d8-9df8-4595-b157-bc6b5aa742bc)
    - GRAD-CAM 사진
    - ![image](https://github.com/user-attachments/assets/eb3e2c12-1bbc-42b1-9540-11079e0cca04)
    - CAM 바운딩 박스
    - ![image](https://github.com/user-attachments/assets/fa58fae3-2ab1-449c-80b8-7ae46e712a8b)
    - GRAD-CAM 바운딩 박스
    -![image](https://github.com/user-attachments/assets/0d03c4a9-43c9-4c9e-b780-597c50b068e1)
    - IOU

- [O]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - ![image](https://github.com/user-attachments/assets/4524f02d-9056-43d0-8fed-8a2655618e50)
    - CAM을 생성하는 부분에 주석을 달아 이해를 시켰다.

- [O]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 코드에 나와있진 않지만, ImageNet으로 받아왔던 기존 이미지를 False로 두고 가중치가 없는 상태에서 모델을 학습시켰다.

- [O]  **4. 회고를 잘 작성했나요?**
    - ![image](https://github.com/user-attachments/assets/c75f407c-5540-49ca-ab8c-2157fdd88fe9)


- [O]  **5. 코드가 간결하고 효율적인가요?**
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화/모듈화했는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        - ![image](https://github.com/user-attachments/assets/5a7554eb-3124-4749-adf8-dfe4bd69f675)
        - 함수로 정규화 및 리사이징을 시행


# 회고(참고 링크 및 코드 개선)
```
결과와 실험 결과를 분석한 것이 좋은 자세인 것 같다.
또한 이미지를 불러오는 데 있어서 새로운 시도를 한 것이 좋았다.
전체적으로 깔끔한 코드였다.
```
