setInterval(()=>{

    let currentDate = new Date()
    let birthday = new Date('12 16, 2001 11:15:00')
    let currentYear = currentDate.getFullYear()
    let birthdayYear = birthday.getFullYear()
    let currentMonth = currentDate.getMonth()
    let birthdayMonth = birthday.getMonth()
    let currentDay = currentDate.getDate()
    let birthdayDay = birthday.getDate()
    
    function newbdayyear(currentMonth,birthdayMonth,currentDay,birthdayDay){
        if(currentMonth=birthdayMonth , currentDay>birthdayDay){
            let newbdayyear1 = currentYear-birthdayYear
            return newbdayyear1

        }
        else{
            let newbdayyear2 = currentYear-birthdayYear-1
            return newbdayyear2
        }
    }
    let month = Math.abs(currentMonth+1)
    function newbdaydate (){
        if(birthdayDay>=currentDay){
            let newbday1 = birthdayDay+currentDay-1
            return newbday1
        }
        else{
             let newbday2 = currentDay-birthdayDay
             return newbday2
        }
    }
    
    let btn=document.querySelector('.btn')
    
    btn.innerHTML=`${newbdayyear() + "Year"} ${month+ "Month"}  ${newbdaydate() + "Days" } ${currentDate.getHours() + 'Hours'} : ${currentDate.getMinutes()+'Minutes'}: ${currentDate.getSeconds()+ 'Seconds'}: ${currentDate.getMilliseconds()+'Milliseconds'}`
    },1)


