from django.db import models

class Club(models.Model):
    name = models.CharField("NAME", max_length=50) # 동아리 이름
    description = models.CharField("DESCRIPTION", max_length=100, blank=True, null= True) # 동아리 요약(해쉬태그 형식)
    content = models.TextField("CONTENT", blank=True, null=True) # 동아리 소개글
    information = models.TextField("INFORMATION", blank=True, null=True) # 동아리 부스 정보
    location = models.CharField("LOCATION", max_length=50) # 동아리 부스 위치(grassField, )
    contact = models.CharField("CONTACT", max_length=50, blank=True, null=True) # 동아리 인스타 주소
    image = models.ImageField("IMAGE", upload_to="club/", blank=True, null=True) # 동아리 이미지
    date= models.IntegerField("DATE") # 부스 운영 날짜
    belong = models.CharField("BELONG", max_length=50, blank=True, null=True) # 주점 소속
    distinct=models.IntegerField("DIS", blank=True, null=True)
    # 0: 수, 1: 목, 2: 금
    
    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubs"

    def __str__(self):
        return self.name


class Pub(models.Model):
    name = models.CharField("NAME", max_length=50) # 주점 이름
    description = models.CharField("DESCRIPTION", max_length=100, blank=True, null= True) # 주점 요약(해쉬태그 형식)
    content = models.TextField("CONTENT", blank=True, null=True) # 주점 소개글
    belong = models.CharField("BELONG", max_length=50) # 주점 소속
    location = models.CharField("LOCATION", max_length=50) # 주점 부스 위치
    contact = models.CharField("CONTACT", max_length=50, blank=True, null=True) # 주점 인스타 주소
    image = models.ImageField("IMAGE", upload_to="pub/", blank=True, null=True) # 주점 이미지
    date= models.IntegerField("DATE") # 부스 운영 날짜
    distinct=models.IntegerField("DIS", blank=True, null=True)
    # 0: 수, 1: 목, 2: 금
    

    class Meta:
        verbose_name = "Pub"
        verbose_name_plural = "Pubs"

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    pub = models.ForeignKey(Pub, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("NAME", max_length=50)
    decription = models.CharField("DESCRIPTION", max_length=100, blank=True, null= True)
    price = models.CharField("PRICE", max_length=50, blank=True, null= True)

    def __str__(self):
        return self.name