import sys
import asyncio
from PyQt5.QtWidgets import QMainWindow,QDialog,QApplication
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymongo
import json
from pymongo import MongoClient

try:
    client =  pymongo.MongoClient(
            'mongodb+srv://puttanpal:puttanpal@cluster0.l891v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = client["hospital"]
    admits = db["admits"]
    bills = db['bills']
    patientRecord = db['patientRecord']
    revenue_Collection = db['revenue']
    rooms_Collection = db['rooms']
    staff = db['staff']
    staffDuty_Collection = db['staffDuty']
    vehichle_Collection = db['vehichle']

except Exception as e:
    print(e)

class Admit(QMainWindow):
    def __init__(self):
        super(Admit, self).__init__()
        loadUi('Admit.ui',self)
        self.menuAction1 = QAction(self)
        self.menuAction1.triggered.connect(self.PatientRecordUP)
        self.menuAction2 = QAction(self)
        self.menuAction2.triggered.connect(self.LoginUP)
        self.menuAction3 = QAction(self)
        self.menuAction3.triggered.connect(self.staffRecordUP)
        self.menuAction4 = QAction(self)
        self.menuAction4.triggered.connect(self.vehichleDutyUP)
        self.menuAction5 = QAction(self)
        self.menuAction5.triggered.connect(self.RoomsUP)
        self.menuAction6 = QAction(self)
        self.menuAction6.triggered.connect(self.BillUP)
        self.menuAction7 = QAction(self)
        self.menuAction7.triggered.connect(self.AdmitUP)
        self.menuAction8 = QAction(self)
        self.menuAction8.triggered.connect(self.staffDutyUP)
        self.menuAction9 = QAction(self)
        self.menuAction9.triggered.connect(self.RevenueUP)

       #attaching the listeners to the menu item
        self.PRecordMenu.addAction(self.menuAction1)
        self.LoginMenu.addAction(self.menuAction2)
        self.StaffMenu.addAction(self.menuAction3)
        self.VehichleMenu.addAction(self.menuAction4)
        self.RoomsMenu.addAction(self.menuAction5)
        self.BillingMenu.addAction(self.menuAction6)
        self.AdmitMenu.addAction(self.menuAction7)
        self.StaffDutyMenu.addAction(self.menuAction8)
        self.RevenueMenu.addAction(self.menuAction9)
        self.AdmitBtn.clicked.connect(self.admitUser)

    def admitUser(self):
        try:
            name = self.NameEdit.text()
            gender = self.GenderCombo.currentText()
            age = self.AgeSpin.value()
            contact = self.ContacrEdit.text()
            emergency = self.EmergencyEdit.text()
            family = self.FamilyEdit.text()
            ailment = self.AilmentEdit.toPlainText()
            roomNumber = self.RoomNumberEdit.text()
            roomType = self.RoomCombo.currentText()
            assignedStaff = self.StaffEdit.toPlainText()
            email = self.EmailEdit.text()
            medicalHistory = self.MedicHistoryEdit.toPlainText()
            if name == '' or gender == '' or age == '' or contact == '' or emergency == '' or family == '' or ailment == '' or roomNumber == '' or roomType == ''or assignedStaff == '' or email == '' or medicalHistory == '' :
                self.showMessage("plz fill in all the details","Fill All details")
            else:
                doc={"id":f"{name}_{gender}_{age}","name":name,"gender":gender,"age":age,"contact":contact,
                     "emergency":emergency,"family":family,"ailment":ailment,"roomNumber":roomNumber,
                     "roomType":roomType,"assignedStaff":assignedStaff,"email":email,
                     "medicalhistory":medicalHistory}
                try:
                    admits.insert_one(doc)
                    self.clearData()
                    self.showMessage('The record was successfully updated!!','Success!')
                except Exception as e:
                    print(e)
                    self.showMessage()


        except Exception as e:
            print(e)
    def clearData(self):
        self.NameEdit.clear()
        self.GenderCombo.SelectedIndex = 0;
        self.AgeSpin.clear()
        self.ContacrEdit.clear()
        self.EmergencyEdit.clear()
        self.FamilyEdit.clear()
        self.AilmentEdit.clear()
        self.RoomNumberEdit.clear()
        self.RoomCombo.SelectedIndex=0
        self.StaffEdit.clear()
        self.EmailEdit.clear()
        self.MedicHistoryEdit.clear()
        self.EmailEdit.clear()
        self.MedicHistoryEdit.clear()

    def showMessage(self,msg:str,title:str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')

    def AdmitUP(self):
        widget.setCurrentIndex(6)
    def BillUP(self):
        widget.setCurrentIndex(5)
    def LoginUP(self):
        widget.setCurrentIndex(1)
    def PatientRecordUP(self):
        widget.setCurrentIndex(0)
    def RevenueUP(self):
        widget.setCurrentIndex(8)
    def RoomsUP(self):
        widget.setCurrentIndex(4)
    def staffDutyUP(self):
        widget.setCurrentIndex(7)
    def staffRecordUP(self):
        widget.setCurrentIndex(2)
    def vehichleDutyUP(self):
        widget.setCurrentIndex(3)

class Bill(QMainWindow):
    def __init__(self):
        super(Bill, self).__init__()
        loadUi('Bill.ui',self)
        self.menuAction1 = QAction(self)
        self.menuAction1.triggered.connect(self.PatientRecordUP)
        self.menuAction2 = QAction(self)
        self.menuAction2.triggered.connect(self.LoginUP)
        self.menuAction3 = QAction(self)
        self.menuAction3.triggered.connect(self.staffRecordUP)
        self.menuAction4 = QAction(self)
        self.menuAction4.triggered.connect(self.vehichleDutyUP)
        self.menuAction5 = QAction(self)
        self.menuAction5.triggered.connect(self.RoomsUP)
        self.menuAction6 = QAction(self)
        self.menuAction6.triggered.connect(self.BillUP)
        self.menuAction7 = QAction(self)
        self.menuAction7.triggered.connect(self.AdmitUP)
        self.menuAction8 = QAction(self)
        self.menuAction8.triggered.connect(self.staffDutyUP)
        self.menuAction9 = QAction(self)
        self.menuAction9.triggered.connect(self.RevenueUP)
        self.PRecordMenu.addAction(self.menuAction1)
        self.LoginMenu.addAction(self.menuAction2)
        self.StaffMenu.addAction(self.menuAction3)
        self.VehichleMenu.addAction(self.menuAction4)
        self.RoomsMenu.addAction(self.menuAction5)
        self.BillingMenu.addAction(self.menuAction6)
        self.AdmitMenu.addAction(self.menuAction7)
        self.StaffDutyMenu.addAction(self.menuAction8)
        self.RevenueMenu.addAction(self.menuAction9)
        self.PayBtn.clicked.connect(self.Payment)
        self.pushButton.clicked.connect(self.refresh)#this is ther action to slot connection for the the refresh button
        self.AddRow.clicked.connect(self.addRow)
        self.patient=''

    def getPid(self):
        self.patient=self.PidEntry.text()
        if self.patient == '':
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText('Enter the patient ID')
            msgBox.setWindowTitle('Patient ID')
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                print('OK clicked')


    def Payment(self):
        try:
            self.getPid()
            rowCount = self.tableWidget.rowCount()
            data=list()
            for i in range(0, rowCount):
                row=dict()
                count=0
                for j in range(0,7):
                    try:
                        val = self.tableWidget.item(i, j).text()
                    except Exception as e:
                        val=''
                        count=count+1

                    if j == 0:
                        row['Day']=val
                    elif j == 1:
                        row['Room Charge'] =val
                    elif j == 2:
                        row['Medication Cost'] =val
                    elif j == 3:
                        row['Operation Cost'] =val
                    elif j == 4:
                        row['Private Nurse'] =val
                    elif j == 5:
                        row['GST'] =val
                    elif j == 6:
                        row['SGST'] =val
                    elif j == 7:
                        row['Total'] =val
                if count<=1:
                    data.append(row)
            self.writeData(data)

        except Exception as e:
            print(e)

    def writeData(self,data):
        if self.patient !='':
            bills.insert_one({'Pid':self.patient,'days':data})
            self.tableWidget.setRowCount(len(data))

    def refresh(self):
        self.PidEntry.clear()
        self.tableWidget.setRowCount(0)

    def addRow(self):
        try:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowCount)


        except Exception as e:
            print(e)

    def AdmitUP(self):
        widget.setCurrentIndex(6)

    def BillUP(self):
        widget.setCurrentIndex(5)

    def LoginUP(self):
        widget.setCurrentIndex(1)

    def PatientRecordUP(self):
        widget.setCurrentIndex(0)

    def RevenueUP(self):
        widget.setCurrentIndex(8)

    def RoomsUP(self):
        widget.setCurrentIndex(4)

    def staffDutyUP(self):
        widget.setCurrentIndex(7)

    def staffRecordUP(self):
        widget.setCurrentIndex(2)

    def vehichleDutyUP(self):
        widget.setCurrentIndex(3)

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('Login.ui',self)
        self.menuAction1 = QAction(self)
        self.menuAction1.triggered.connect(self.PatientRecordUP)
        self.menuAction2 = QAction(self)
        self.menuAction2.triggered.connect(self.LoginUP)
        self.menuAction3 = QAction(self)
        self.menuAction3.triggered.connect(self.staffRecordUP)
        self.menuAction4 = QAction(self)
        self.menuAction4.triggered.connect(self.vehichleDutyUP)
        self.menuAction5 = QAction(self)
        self.menuAction5.triggered.connect(self.RoomsUP)
        self.menuAction6 = QAction(self)
        self.menuAction6.triggered.connect(self.BillUP)
        self.menuAction7 = QAction(self)
        self.menuAction7.triggered.connect(self.AdmitUP)
        self.menuAction8 = QAction(self)
        self.menuAction8.triggered.connect(self.staffDutyUP)
        self.menuAction9 = QAction(self)
        self.menuAction9.triggered.connect(self.RevenueUP)
        self.PRecordMenu.addAction(self.menuAction1)
        self.LoginMenu.addAction(self.menuAction2)
        self.StaffMenu.addAction(self.menuAction3)
        self.VehichleMenu.addAction(self.menuAction4)
        self.RoomsMenu.addAction(self.menuAction5)
        self.BillingMenu.addAction(self.menuAction6)
        self.AdmitMenu.addAction(self.menuAction7)
        self.StaffDutyMenu.addAction(self.menuAction8)
        self.RevenueMenu.addAction(self.menuAction9)
        self.LoginBtn.clicked.connect(self.authUser)

    #will be using staff datbase for authenticating the login of a staff
    def authUser(self):
        role = self.StaffCombo.currentText()
        id=self.StaffIDEdit.text()
        password= self.PasswordEdit.text()
        result=None
        try:
            result = staff.find_one({"role": role, "id": id, "password": password},{'_id':0})
            if result != None:
                authenticated = True
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msg=f'id:{result["id"]}\nname:{result["name"]}\nage:{result["age"]}\ngender:{result["gender"]}\nrole:{result["role"]}'
                msgBox.setText(f'You are successfully authenticated \n {msg}')
                msgBox.setWindowTitle('Successful auuthentication')
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    print('OK clicked')
        except Exception as e:
            print(e)
    def AdmitUP(self):
        widget.setCurrentIndex(6)

    def BillUP(self):
        widget.setCurrentIndex(5)

    def LoginUP(self):
        widget.setCurrentIndex(1)

    def PatientRecordUP(self):
        widget.setCurrentIndex(0)

    def RevenueUP(self):
        widget.setCurrentIndex(8)

    def RoomsUP(self):
        widget.setCurrentIndex(4)

    def staffDutyUP(self):
        widget.setCurrentIndex(7)

    def staffRecordUP(self):
        widget.setCurrentIndex(2)

    def vehichleDutyUP(self):
        widget.setCurrentIndex(3)

class PatientRecord(QMainWindow):
    def __init__(self):
        super(PatientRecord, self).__init__()
        loadUi('PatientRecord.ui',self)
        self.menuAction1 = QAction(self)
        self.menuAction1.triggered.connect(self.PatientRecordUP)
        self.menuAction2 = QAction(self)
        self.menuAction2.triggered.connect(self.LoginUP)
        self.menuAction3 = QAction(self)
        self.menuAction3.triggered.connect(self.staffRecordUP)
        self.menuAction4 = QAction(self)
        self.menuAction4.triggered.connect(self.vehichleDutyUP)
        self.menuAction5 = QAction(self)
        self.menuAction5.triggered.connect(self.RoomsUP)
        self.menuAction6 = QAction(self)
        self.menuAction6.triggered.connect(self.BillUP)
        self.menuAction7 = QAction(self)
        self.menuAction7.triggered.connect(self.AdmitUP)
        self.menuAction8 = QAction(self)
        self.menuAction8.triggered.connect(self.staffDutyUP)
        self.menuAction9 = QAction(self)
        self.menuAction9.triggered.connect(self.RevenueUP)
        self.PRecordMenu.addAction(self.menuAction1)
        self.LoginMenu.addAction(self.menuAction2)
        self.StaffMenu.addAction(self.menuAction3)
        self.VehichleMenu.addAction(self.menuAction4)
        self.RoomsMenu.addAction(self.menuAction5)
        self.BillingMenu.addAction(self.menuAction6)
        self.AdmitMenu.addAction(self.menuAction7)
        self.StaffDutyMenu.addAction(self.menuAction8)
        self.RevenueMenu.addAction(self.menuAction9)
        self.SearchBtn.clicked.connect(self.filterData)
        self.SearchBtn_2.clicked.connect(self.filterData2)
        self.data = dict({})
        self.count = 0
        self.getData()
        self.populateTable()
        self.button.clicked.connect(self.refreshData)
        # this function will fetch all the revenue data from the database

    def refreshData(self):
        self.getData()
        self.populateTable()
    def getData(self):
        self.data = admits.find({}, {'_id': 0,"id":0})
        self.count = admits.count_documents({})

    def populateTable(self):
        self.TableWidget.setRowCount(self.count)
        row = 0
        for item in self.data:
            col = 0
            for key in item:
                self.TableWidget.setItem(row, col, QTableWidgetItem(f'{item[key]}'))
                col = col + 1
            row = row + 1
    def filterData(self):
        patientId=self.PIDEntry.text()
        self.data = admits.find({"id":patientId}, {'_id': 0,"id":0})
        self.count = admits.count_documents({})
        self.populateTable()

    def filterData2(self):
        patientName=self.PIDEntry_2.text()
        self.data = admits.find({"name":patientName}, {'_id': 0,"id":0})
        self.count = admits.count_documents({})
        self.populateTable()



    def AdmitUP(self):
        widget.setCurrentIndex(6)

    def BillUP(self):
        widget.setCurrentIndex(5)

    def LoginUP(self):
        widget.setCurrentIndex(1)

    def PatientRecordUP(self):
        widget.setCurrentIndex(0)

    def RevenueUP(self):
        widget.setCurrentIndex(8)

    def RoomsUP(self):
        widget.setCurrentIndex(4)

    def staffDutyUP(self):
        widget.setCurrentIndex(7)

    def staffRecordUP(self):
        widget.setCurrentIndex(2)

    def vehichleDutyUP(self):
        widget.setCurrentIndex(3)

class Revenue(QMainWindow):
    def __init__(self):
        super(Revenue, self).__init__()
        loadUi('Revenue.ui',self)
        self.menuAction1 = QAction(self)
        self.menuAction1.triggered.connect(self.PatientRecordUP)
        self.menuAction2 = QAction(self)
        self.menuAction2.triggered.connect(self.LoginUP)
        self.menuAction3 = QAction(self)
        self.menuAction3.triggered.connect(self.staffRecordUP)
        self.menuAction4 = QAction(self)
        self.menuAction4.triggered.connect(self.vehichleDutyUP)
        self.menuAction5 = QAction(self)
        self.menuAction5.triggered.connect(self.RoomsUP)
        self.menuAction6 = QAction(self)
        self.menuAction6.triggered.connect(self.BillUP)
        self.menuAction7 = QAction(self)
        self.menuAction7.triggered.connect(self.AdmitUP)
        self.menuAction8 = QAction(self)
        self.menuAction8.triggered.connect(self.staffDutyUP)
        self.menuAction9 = QAction(self)
        self.menuAction9.triggered.connect(self.RevenueUP)
        self.PRecordMenu.addAction(self.menuAction1)
        self.LoginMenu.addAction(self.menuAction2)
        self.StaffMenu.addAction(self.menuAction3)
        self.VehichleMenu.addAction(self.menuAction4)
        self.RoomsMenu.addAction(self.menuAction5)
        self.BillingMenu.addAction(self.menuAction6)
        self.AdmitMenu.addAction(self.menuAction7)
        self.StaffDutyMenu.addAction(self.menuAction8)
        self.RevenueMenu.addAction(self.menuAction9)
        self.data = dict({})
        self.count =0
        self.getData()
        self.populateTable()
        self.FindBtn.clicked.connect(self.filterData)
        self.RefBtn.clicked.connect(self.refreshData)
#this function will fetch all the revenue data from the database
    def refreshData(self):
        self.getData()
        self.populateTable()
    def getData(self):
        self.data=revenue_Collection.find({},{'_id':0})
        self.count=revenue_Collection.count_documents({})
    def populateTable(self):
        self.tableWidget.setRowCount(self.count)
        row=0
        for item in self.data:
            col=0
            for key in item:
                self.tableWidget.setItem(row,col,QTableWidgetItem(f'{item[key]}'))
                col=col+1
            row=row+1
    def filterData(self):
        try:
            month = self.MonthCombo.currentText()
            year = self.YearCombo.itemText(self.YearCombo.currentIndex())
            self.data = revenue_Collection.find({'Month':month,'Year':year}, {'_id': 0})
            self.count = revenue_Collection.count_documents({'Month':month,'Year':year})
            self.populateTable()

        except Exception as e:
            print(e)


    def AdmitUP(self):
        widget.setCurrentIndex(6)

    def BillUP(self):
        widget.setCurrentIndex(5)

    def LoginUP(self):
        widget.setCurrentIndex(1)

    def PatientRecordUP(self):
        widget.setCurrentIndex(0)

    def RevenueUP(self):
        widget.setCurrentIndex(8)

    def RoomsUP(self):
        widget.setCurrentIndex(4)

    def staffDutyUP(self):
        widget.setCurrentIndex(7)

    def staffRecordUP(self):
        widget.setCurrentIndex(2)

    def vehichleDutyUP(self):
        widget.setCurrentIndex(3)

class Rooms(QMainWindow):
    def __init__(self):
        super(Rooms, self).__init__()
        loadUi('Rooms.ui',self)
        self.menuAction1 = QAction(self)
        self.menuAction1.triggered.connect(self.PatientRecordUP)
        self.menuAction2 = QAction(self)
        self.menuAction2.triggered.connect(self.LoginUP)
        self.menuAction3 = QAction(self)
        self.menuAction3.triggered.connect(self.staffRecordUP)
        self.menuAction4 = QAction(self)
        self.menuAction4.triggered.connect(self.vehichleDutyUP)
        self.menuAction5 = QAction(self)
        self.menuAction5.triggered.connect(self.RoomsUP)
        self.menuAction6 = QAction(self)
        self.menuAction6.triggered.connect(self.BillUP)
        self.menuAction7 = QAction(self)
        self.menuAction7.triggered.connect(self.AdmitUP)
        self.menuAction8 = QAction(self)
        self.menuAction8.triggered.connect(self.staffDutyUP)
        self.menuAction9 = QAction(self)
        self.menuAction9.triggered.connect(self.RevenueUP)
        self.PRecordMenu.addAction(self.menuAction1)
        self.LoginMenu.addAction(self.menuAction2)
        self.StaffMenu.addAction(self.menuAction3)
        self.VehichleMenu.addAction(self.menuAction4)
        self.RoomsMenu.addAction(self.menuAction5)
        self.BillingMenu.addAction(self.menuAction6)
        self.AdmitMenu.addAction(self.menuAction7)
        self.StaffDutyMenu.addAction(self.menuAction8)
        self.RevenueMenu.addAction(self.menuAction9)
        self.pushButton.clicked.connect(self.filterData)
        self.data = dict({})
        self.count = 0
        self.getData()
        self.populateTable()
        self.button.clicked.connect(self.refreshData)
        # this function will fetch all the revenue data from the database
    def refreshData(self):
        self.getData()
        self.populateTable()
    def getData(self):
        self.data = rooms_Collection.find({},{'_id':0})
        self.count = rooms_Collection.count_documents({})

    def populateTable(self):
        self.tableWidget.setRowCount(self.count)
        row = 0
        for item in self.data:
            col = 0
            for key in item:
                self.tableWidget.setItem(row, col, QTableWidgetItem(f'{item[key]}'))
                col = col + 1
            row = row + 1
    def filterData(self):
        roomType=self.RoomCombo.currentText()
        self.data = rooms_Collection.find({'Type':roomType}, {'_id': 0})
        self.count = rooms_Collection.count_documents({'Type':roomType})
        self.populateTable()


    def AdmitUP(self):
        widget.setCurrentIndex(6)

    def BillUP(self):
        widget.setCurrentIndex(5)

    def LoginUP(self):
        widget.setCurrentIndex(1)

    def PatientRecordUP(self):
        widget.setCurrentIndex(0)

    def RevenueUP(self):
        widget.setCurrentIndex(8)

    def RoomsUP(self):
        widget.setCurrentIndex(4)

    def staffDutyUP(self):
        widget.setCurrentIndex(7)

    def staffRecordUP(self):
        widget.setCurrentIndex(2)

    def vehichleDutyUP(self):
        widget.setCurrentIndex(3)

class StaffDutty(QMainWindow):
    def __init__(self):
        super(StaffDutty, self).__init__()
        loadUi('StaffDuty.ui',self)
        self.menuAction1 = QAction(self)
        self.menuAction1.triggered.connect(self.PatientRecordUP)
        self.menuAction2 = QAction(self)
        self.menuAction2.triggered.connect(self.LoginUP)
        self.menuAction3 = QAction(self)
        self.menuAction3.triggered.connect(self.staffRecordUP)
        self.menuAction4 = QAction(self)
        self.menuAction4.triggered.connect(self.vehichleDutyUP)
        self.menuAction5 = QAction(self)
        self.menuAction5.triggered.connect(self.RoomsUP)
        self.menuAction6 = QAction(self)
        self.menuAction6.triggered.connect(self.BillUP)
        self.menuAction7 = QAction(self)
        self.menuAction7.triggered.connect(self.AdmitUP)
        self.menuAction8 = QAction(self)
        self.menuAction8.triggered.connect(self.staffDutyUP)
        self.menuAction9 = QAction(self)
        self.menuAction9.triggered.connect(self.RevenueUP)
        self.PRecordMenu.addAction(self.menuAction1)
        self.LoginMenu.addAction(self.menuAction2)
        self.StaffMenu.addAction(self.menuAction3)
        self.VehichleMenu.addAction(self.menuAction4)
        self.RoomsMenu.addAction(self.menuAction5)
        self.BillingMenu.addAction(self.menuAction6)
        self.AdmitMenu.addAction(self.menuAction7)
        self.StaffDutyMenu.addAction(self.menuAction8)
        self.RevenueMenu.addAction(self.menuAction9)
        self.SearcgBtn.clicked.connect(self.filterData1)
        self.data = dict({})
        self.count = 0
        self.data2 = dict({})
        self.count2 = 0
        self.getData()
        self.populateTable()
        # this function will fetch all the revenue data from the database

    def getData(self):
        self.data = staffDuty_Collection.find({}, {'_id': 0})
        self.count = staffDuty_Collection.count_documents({})

    def populateTable(self):
        self.DayTabel.setRowCount(self.count)
        row = 0
        for item in self.data:
            col = 0
            for key in item:
                self.DayTabel.setItem(row, col, QTableWidgetItem(f'{item[key]}'))
                col = col + 1
            row = row + 1

    def populateTabl2(self):
        self.tableWidget_2.setRowCount(self.count2)
        row = 0
        for item in self.data2:
            col = 0
            for key in item:
                self.tableWidget_2.setItem(row, col, QTableWidgetItem(f'{item[key]}'))
                col = col + 1
            row = row + 1

    def filterData1(self):
        role=self.StaffCombo.currentText()
        id=self.IdEdit.text()
        print(role,id)
        try:
            self.data2 = staffDuty_Collection.find({"duty":role,"id":id}, {'_id': 0,"Date":1,"id":1,"shift":1,"duty":1,"role":1})
            self.count2 = staffDuty_Collection.count_documents({"duty":role,"id":id})
            self.populateTabl2()
        except Exception as e:
            print(e)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText('Fill in the details first')
            msgBox.setWindowTitle('Invalid inputs')
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                print('OK clicked')

    def AdmitUP(self):
        widget.setCurrentIndex(6)

    def BillUP(self):
        widget.setCurrentIndex(5)

    def LoginUP(self):
        widget.setCurrentIndex(1)

    def PatientRecordUP(self):
        widget.setCurrentIndex(0)

    def RevenueUP(self):
        widget.setCurrentIndex(8)

    def RoomsUP(self):
        widget.setCurrentIndex(4)

    def staffDutyUP(self):
        widget.setCurrentIndex(7)

    def staffRecordUP(self):
        widget.setCurrentIndex(2)

    def vehichleDutyUP(self):
        widget.setCurrentIndex(3)

class StaffRecord(QMainWindow):
    def __init__(self):
        super(StaffRecord, self).__init__()
        loadUi('StaffRecord.ui',self)
        self.menuAction1 = QAction(self)
        self.menuAction1.triggered.connect(self.PatientRecordUP)
        self.menuAction2 = QAction(self)
        self.menuAction2.triggered.connect(self.LoginUP)
        self.menuAction3 = QAction(self)
        self.menuAction3.triggered.connect(self.staffRecordUP)
        self.menuAction4 = QAction(self)
        self.menuAction4.triggered.connect(self.vehichleDutyUP)
        self.menuAction5 = QAction(self)
        self.menuAction5.triggered.connect(self.RoomsUP)
        self.menuAction6 = QAction(self)
        self.menuAction6.triggered.connect(self.BillUP)
        self.menuAction7 = QAction(self)
        self.menuAction7.triggered.connect(self.AdmitUP)
        self.menuAction8 = QAction(self)
        self.menuAction8.triggered.connect(self.staffDutyUP)
        self.menuAction9 = QAction(self)
        self.menuAction9.triggered.connect(self.RevenueUP)
        self.PRecordMenu.addAction(self.menuAction1)
        self.LoginMenu.addAction(self.menuAction2)
        self.StaffMenu.addAction(self.menuAction3)
        self.VehichleMenu.addAction(self.menuAction4)
        self.RoomsMenu.addAction(self.menuAction5)
        self.BillingMenu.addAction(self.menuAction6)
        self.AdmitMenu.addAction(self.menuAction7)
        self.StaffDutyMenu.addAction(self.menuAction8)
        self.RevenueMenu.addAction(self.menuAction9)
        self.SearchBtn.clicked.connect(self.filterData)
        self.data = dict({})
        self.count = 0
        self.getData()
        self.populateTable()
        # this function will fetch all the revenue data from the database

    def getData(self):
        self.data = staff.find({}, {'_id': 0})
        self.count = staff.count_documents({})

    def populateTable(self):
        self.DetailsTable.setRowCount(self.count)
        row = 0
        for item in self.data:
            col = 0
            for key in item:
                self.DetailsTable.setItem(row, col, QTableWidgetItem(f'{item[key]}'))
                col = col + 1
            row = row + 1
    def filterData(self):
        role=self.StaffCombo.currentText()
        id=self.IDEdit.text()
        try:
            data = staff.find_one({"role": role, "id": id}, {'_id': 0})
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            detail1=f'This is the staff details you searched for \n' \
                    f'id: {data["id"]}\nname:{data["name"]}\nage:{data["age"]}\ngender:{data["gender"]}\nrole:{data["role"]}' \
                    f'\njoined:{data["joined"]}\nstatus:{data["status"]}'
            certificates=""
            for el in data['certifications']:
                certificates=certificates+el+"\n"

            msgBox.setText(f'{detail1} \n certifications:{certificates}')
            msgBox.setWindowTitle('Staff Details')
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                print('OK clicked')
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText('Fill in the details first')
            msgBox.setWindowTitle('Invalid inputs')
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                print('OK clicked')





    def AdmitUP(self):
        widget.setCurrentIndex(6)

    def BillUP(self):
        widget.setCurrentIndex(5)

    def LoginUP(self):
        widget.setCurrentIndex(1)

    def PatientRecordUP(self):
        widget.setCurrentIndex(0)

    def RevenueUP(self):
        widget.setCurrentIndex(8)

    def RoomsUP(self):
        widget.setCurrentIndex(4)

    def staffDutyUP(self):
        widget.setCurrentIndex(7)

    def staffRecordUP(self):
        widget.setCurrentIndex(2)

    def vehichleDutyUP(self):
        widget.setCurrentIndex(3)

class VehichleDuty(QMainWindow):
    def __init__(self):
        super(VehichleDuty, self).__init__()
        loadUi('VehichleDuty.ui',self)
        self.menuAction1 = QAction(self)
        self.menuAction1.triggered.connect(self.PatientRecordUP)
        self.menuAction2 = QAction(self)
        self.menuAction2.triggered.connect(self.LoginUP)
        self.menuAction3 = QAction(self)
        self.menuAction3.triggered.connect(self.staffRecordUP)
        self.menuAction4 = QAction(self)
        self.menuAction4.triggered.connect(self.vehichleDutyUP)
        self.menuAction5 = QAction(self)
        self.menuAction5.triggered.connect(self.RoomsUP)
        self.menuAction6 = QAction(self)
        self.menuAction6.triggered.connect(self.BillUP)
        self.menuAction7 = QAction(self)
        self.menuAction7.triggered.connect(self.AdmitUP)
        self.menuAction8 = QAction(self)
        self.menuAction8.triggered.connect(self.staffDutyUP)
        self.menuAction9 = QAction(self)
        self.menuAction9.triggered.connect(self.RevenueUP)
        self.PRecordMenu.addAction(self.menuAction1)
        self.LoginMenu.addAction(self.menuAction2)
        self.StaffMenu.addAction(self.menuAction3)
        self.VehichleMenu.addAction(self.menuAction4)
        self.RoomsMenu.addAction(self.menuAction5)
        self.BillingMenu.addAction(self.menuAction6)
        self.AdmitMenu.addAction(self.menuAction7)
        self.StaffDutyMenu.addAction(self.menuAction8)
        self.RevenueMenu.addAction(self.menuAction9)
        self.SearchBtn.clicked.connect(self.findData)#connecting an action to the custom slot
        self.data = dict({})
        self.count = 0
        self.getData()
        self.populateTable()
        # this function will fetch all the revenue data from the database

    def getData(self):
        self.data = vehichle_Collection.find({}, {'_id': 0})
        self.count = vehichle_Collection.count_documents({})

    def populateTable(self):
        self.tableWidget.setRowCount(self.count)
        row = 0
        for item in self.data:
            col = 0
            for key in item:
                self.tableWidget.setItem(row, col, QTableWidgetItem(f'{item[key]}'))
                col = col + 1
            row = row + 1
    def populateTable2(self):
        self.PersonTable.setRowCount(self.count)
        row = 0
        for item in self.data:
            col = 0
            for key in item:
                self.PersonTable.setItem(row, col, QTableWidgetItem(f'{item[key]}'))
                col = col + 1
            row = row + 1
    def findData(self):
        driverId=self.DriverIDEdit.text()
        if driverId != '':
            self.data = vehichle_Collection.find({"Driver_Id":driverId}, {'_id': 0,'name':1,'vehichle':1,'shift':1,'Date':1})
            self.count = vehichle_Collection.count_documents({})
            self.populateTable2()

        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText('Enter teh driver Id first')
            msgBox.setWindowTitle('Invalid ID')
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                print('OK clicked')



    def AdmitUP(self):
        widget.setCurrentIndex(6)

    def BillUP(self):
        widget.setCurrentIndex(5)

    def LoginUP(self):
        widget.setCurrentIndex(1)

    def PatientRecordUP(self):
        widget.setCurrentIndex(0)

    def RevenueUP(self):
        widget.setCurrentIndex(8)

    def RoomsUP(self):
        widget.setCurrentIndex(4)

    def staffDutyUP(self):
        widget.setCurrentIndex(7)

    def staffRecordUP(self):
        widget.setCurrentIndex(2)

    def vehichleDutyUP(self):
        widget.setCurrentIndex(3)


app=QApplication(sys.argv)
admit = Admit()
bill = Bill()
login = Login()
patientRecord = PatientRecord()
revenue = Revenue()
rooms = Rooms()
staffDuty = StaffDutty()
staffRecord = StaffRecord()
vehichleDuty = VehichleDuty()
widget=QtWidgets.QStackedWidget()
widget.addWidget(patientRecord)
widget.addWidget(login)
widget.addWidget(staffRecord)
widget.addWidget(vehichleDuty)
widget.addWidget(rooms)
widget.addWidget(bill)
widget.addWidget(admit)
widget.addWidget(staffDuty)
widget.addWidget(revenue)
widget.setFixedWidth(1300)
widget.setFixedHeight(1000)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting the app..")
