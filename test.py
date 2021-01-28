#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/4 17:49
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import wmi


c = wmi.WMI()

# # 硬盘序列号
for physical_disk in c.Win32_DiskDrive():
    print(physical_disk.SerialNumber)

# CPU序列号
for cpu in c.Win32_Processor():
    print(cpu.ProcessorId.strip())

# 主板序列号
for board_id in c.Win32_BaseBoard():
    print(board_id.SerialNumber)

# mac地址
for mac in c.Win32_NetworkAdapter():
    print(mac.MACAddress)

# bios序列号
for bios_id in c.Win32_BIOS():
    print(bios_id.SerialNumber.strip)