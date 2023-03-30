#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist

def sin_dalga_hareketi(turtle_hiz, genlik, frekans, faz, sure):
    """
    Turtle'ı bir sinüs dalga hareketi yapacak şekilde hareket ettiren Twist mesajlarını
    turtle_hiz konusuna yayınlar.
    """
    # düğümü ve yayıncıyı başlat
    rospy.init_node('sin_dalga_hareketi', anonymous=True)
    vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    baslangic_zamani = rospy.Time.now()
    while (rospy.Time.now() - baslangic_zamani).to_sec() < sure:
        # x ve y pozisyonlarını bir sinüs dalga fonksiyonu kullanarak hesapla
        t = (rospy.Time.now() - baslangic_zamani).to_sec()
        x = genlik * math.sin(2 * math.pi * frekans * t + faz)
        y = 0.0

        # yeni pozisyona gitmek için gerekli olan lineer ve açısal hızı hesapla
        vel = Twist()
        vel.linear.x = 2.0 # Lineer hızı sabit bir değere ayarla
        vel.angular.z = (x - turtle_hiz.linear.x) / 2.0 # Açısal hızı yeni pozisyona göre hesapla

        # Hız komutunu yayınla
        vel_pub.publish(vel)

        rate.sleep()

if __name__ == '__main__':
    # Sinüs dalga hareketi için parametreleri ayarla
    genlik = 2.0
    frekans = 1.0
    faz = 0.0
    sure = 30.0

    # Turtle hızı mesajını oluştur
    turtle_hiz = Twist()
    turtle_hiz.linear.x = 0.0
    turtle_hiz.linear.y = 0.0
    turtle_hiz.linear.z = 0.0
    turtle_hiz.angular.x

