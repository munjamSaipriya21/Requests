import requests
import json
result=requests.get("https://saral.navgurukul.org/api/courses")
data=result.json()

with open("availablecourses.json","w") as f:
    json.dump(data,f,indent=4)

def option(select,var1,slug,data2):
    while True: 
        a=var1
        print("*******")
        options=input("enter your options : up, next, exit back   !")
        if options=="up":
            print(a)
            a-=1
            req=requests.get("https://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getbyslug?slug = "+str(slug[a]))
            x=req.json()
    #         print("content",x["content"])    
            while True:
                available_letters = req(letters_gimport requests
import os
import json

def isFileAvailable(fileName):
    return os.path.exists(fileName)
def readJsonFile(fileName):
    with open(fileName,"r") as f:
        return json.load(f)
def createJsonFile(fileName,responseOfCoursesInText):
    with open(fileName,"w") as f:
        data=json.loads(responseOfCoursesInText)
        json.dump(data,f,indent=4)
def printingCourses(data):
    availableCourses=data["availableCourses"]
    index=1
    for i in availableCourses:
        print(index,":",i["name"],"-",i["id"])
        listOfCourseIds.append(i["id"])

        index+=1
    print("listofCourseIds")
def printingExercises(d,listOfslugs):
    responseOfExercises=(d['data'])
    for i in responseOfExercises:
        print("parent Exercise",i["name"])
        listOfslugs.append(i["slug"])
        if len(i["childExercises"])>0:
            for j in i["childExercises"]:
                listOfslugs.append(j["slug"])
                # print("child exercies -", j["name"])
        else:
            print("there is no childexersise[]")
        print(listOfslugs)

def PrintingSlugs(data):
    index=1
    for i in data:
        print(index,":",i)
        index+=1

def CallingSlugApi(slugNumber,listOfCourseIds,userSelectedCourse,listOfslugs):
    responseOfSlug=requests.get("https://saral.navgurukul.org/api/courses/"+str(listOfCourseIds[userSelectedCourse-1])+"/exercise/getBySlug?slug="+str(listOfslugs[slugNumber-1]))
    print(responseOfSlug.text)

listOfCourseIds=[]



def main():
    listOfslugs=[]
    fileName="courses.json"
    if isFileAvailable(fileName):
        data=readJsonFile(fileName)
        printingCourses(data)
    else:
        responseOfCourses=requests.get("https://saral.navgurukul.org/api/courses")
        responseOfCoursesInText=responseOfCourses.text
        createJsonFile(fileName,responseOfCoursesInText)
        data=readJsonFile(fileName)
        printingCourses(data)

    userSelectedCourse=int(input("select a course: "))

    fileNameOfExercise="Exercise_"+str(listOfCourseIds[userSelectedCourse+1])+".json"
    
    if isFileAvailable(fileNameOfExercise):
        data=readJsonFile(fileNameOfExercise)
        printingExercises(data,listOfslugs)
    else:
        print(listOfCourseIds[userSelectedCourse-1])
        responseOfCourseExercies=requests.get("https://saral.navgurukul.org/api/courses/"+str(listOfCourseIds[userSelectedCourse-1])+"/exercises")
        # print(responseOfCourseExercies,"ammulu",)
        responseOfExerciseCoursesInText=responseOfCourseExercies.text
        createJsonFile(fileNameOfExercise,responseOfExerciseCoursesInText)
        data=readJsonFile(fileNameOfExercise)
        # printingExercises(data,listOfslugs)

    PrintingSlugs(listOfslugs)    
    userSelectedSlug=int(input("select a slug: "))
    print(listOfCourseIds[userSelectedCourse-1])
    print("*")
    print(listOfslugs[userSelectedSlug-1])
    print("*")
    CallingSlugApi(userSelectedSlug,listOfCourseIds,userSelectedCourse,listOfslugs)

    seeAgain=input("enter what you want to do:- \n1. up :-\n2. Next:- \n3. Pre :- \n4. stop :-")

    if seeAgain=="up":
        print("up")
    
    elif seeAgain=="Next":
        slugIncreased=userSelectedSlug+1
        CallingSlugApi(slugIncreased,listOfCourseIds,userSelectedCourse,listOfslugs)
    elif seeAgain=="Pre":
        slugIncreased=userSelectedSlug-1
        CallingSlugApi(slugIncreased,listOfCourseIds,userSelectedCourse,listOfslugs)
    else:
        print("Nothing")
main()uessed)
                
                print ("Available letters: ") + available_letters
                print(a)
                if  options=="next":
                    x+=1
                    req=requests.get("https://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getbyslug?slug = "+str(slug[a-1]))
                    x1=req.json()
                    print(a)
                elif options=="back":
                    y=1
                    for dic1 in data2["data"]:
                        print(y,dic1["name"])
                        y+=1
                        print("content",x1["content"])
                        for i in dic1 [" childExercises "]:
                            print("      ",y,i["name"])
                            y+=1
                else:
                    break


def course(): 
    index=0
    for i in data["availableCourses"]:
        print(index+1,i["name"],i["id"])
        index+=1
    for courses in data["availableCourses"]:
        courses=int(input("enter the your index of course = "))
        select=data["availableCourses"][courses-1]["id"]
        var=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise")
        data2=var.json()
        count=1
        slug=[ ]
        for dic_data2 in data2["data"]:
            print(count,dic_data2["name"])
            slug.append(dic_data2["slug"])
            count=count+1
            for child in dic_data2["childExercises"]:
                print(count,child)["name"]
                slug.append(dic_data2["slug"])
                count=count+1
        var2=int(input("select content slug"))
        var3=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise")
        data3=var3.json
        print("content",data3["content"])        
        option (select,var2,slug,data2)
course()