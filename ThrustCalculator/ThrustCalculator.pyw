import tkinter as tk
#Planet Info
planets = ['moon.txt','europa.txt','mars.txt','earth.txt','alien.txt','pertam.txt']
planetData = [0,0,0,0,0,0,0,0,0]
planetIndex = 0
requiredForce = 0
def selectPlanet(Index):
    global planetIndex, planetData
    planetIndex = Index
    setData()
def setData():
    global planetIndex, planetData, planets
    planetData.clear()
    planetFile = open(planets[planetIndex],'r')
    for value in planetFile.readlines():
        planetData.append(float(value))
    #Update ref labels
    ssa = tk.Label(text='Small Grid Small A Thruster: '+str(formatNumber(planetData[1]))).place(x=0,y=110)
    sla = tk.Label(text='Small Grid Large A Thruster: '+str(formatNumber(planetData[2]))).place(x=0,y=130)
    lsa = tk.Label(text='Large Grid Small A Thruster: '+str(formatNumber(planetData[3]))).place(x=0,y=150)
    lla = tk.Label(text='Large Grid Large A Thruster: '+str(formatNumber(planetData[4]))).place(x=0,y=170)
    ssh = tk.Label(text='Small Grid Small H Thruster: '+str(formatNumber(planetData[5]))).place(x=0,y=190)
    slh = tk.Label(text='Small Grid Large H Thruster: '+str(formatNumber(planetData[6]))).place(x=0,y=210)
    lsh = tk.Label(text='Large Grid Small H Thruster: '+str(formatNumber(planetData[7]))).place(x=0,y=230)
    llh = tk.Label(text='Large Grid Large H Thruster: '+str(formatNumber(planetData[8]))).place(x=0,y=250)
    planetFile.close()
def calculateForce(gravity):
    global requiredForce, gridWeightstr, forceDisplay
    gridWeight = int(gridWeightstr.get())
    requiredForce = int(gridWeight*gravity)
    forceDisplay = tk.Label(text='Required Force: '+str(("{:,}".format(requiredForce)))).place(x=0,y=70)
def formatNumber(number):
    return ("{:,}".format(number))
#Window config
win = tk.Tk()
win.title('Space Engineers Thrust Calculator')
win.geometry('275x275')
win.resizable(False,False)
#Buttons
moonButton = tk.Button(text='Moon',command=lambda:selectPlanet(0)).grid(row=0,column=0)
europaButton = tk.Button(text='Europa',command=lambda:selectPlanet(1)).grid(row=0,column=1)
marsButton = tk.Button(text='Mars',command=lambda:selectPlanet(2)).grid(row=0,column=2)
earthButton = tk.Button(text='Earth',command=lambda:selectPlanet(3)).grid(row=0,column=3)
alienButton = tk.Button(text='Alien',command=lambda:selectPlanet(4)).grid(row=0,column=4)
pertamButton = tk.Button(text='Pertam',command=lambda:selectPlanet(5)).grid(row=0,column=5)
#Input
gridWeightstr = tk.StringVar()
tk.Label(text='Weight of grid (Kg):').place(x=0,y=25)
weightInput = tk.Entry(textvariable=gridWeightstr).place(x=110,y=25)
calculate = tk.Button(text='Calculate',command=lambda:calculateForce(planetData[0])).place(x=0,y=45)
#Labels
forceDisplay = tk.Label(text='Required Force: '+str(requiredForce)).place(x=0,y=70)
refHeader = tk.Label(text='Reference Forces:').place(x=0,y=90)
win.mainloop()