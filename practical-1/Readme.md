 1.Calculate the area of a rectangle given its length and width.

BEGIN
    INPUT length of rectangle
    INPUT width of recatangle
    area= length*width
    DISPLAY "area of rectangle " is : area
END    


2.Determine if a number is even or odd.

BEGIN
    FUNCTION even_or_odd(num)
        IF num MOD 2 = 0 THEN
            RETURN "Even"
        ELSE
            RETURN "Odd"
        ENDIF
    END FUNCTION

    DISPLAY even_or_odd(5)
END


3.Find the largest of three given numbers

BEGIN
    INPUT num1
    INPUT num2
    INPUT mum3

    IF num1 >= num2 AND num1 >= num3 THEN
        DISPLAY "The largest number is:", num1
    ELSE IF num2 >= num1 AND b >= num3 THEN
        DISPLAY "The largest number is:", num2
    ELSE
        DISPLAY "The largest number is:", num3
    ENDIF
END


4.Convert temperature from Celsius to Fahrenheit.

BEGIN
    DISPLAY "1. Celsius to Fahrenheit"
    DISPLAY "2. Fahrenheit to Celsius"
    DISPLAY "Choose any one from above (1-2)"

    REPEAT
        INPUT choice

        IF choice = 1 THEN
            INPUT celsius
            conv ← (celsius * 9 / 5) + 32
            DISPLAY "The temperature is", conv, "Fahrenheit"
            EXIT LOOP

        ELSE IF choice = 2 THEN
            INPUT fahrenheit
            conv ← (fahrenheit - 32) * 5 / 9
            DISPLAY "The temperature is", conv, "Celsius"
            EXIT LOOP

        ELSE
            DISPLAY "Error"

