def main():
    ##################################################
    # Comlete your code here
    ##################################################
    reg_hours = 40 
    reg_rate = 18.25
    o_rate = 27.78
    workhours = int( input ('How many hours of work? ') )
    o_hours = workhours - 40 
    reg_wages = reg_hours * reg_rate
    o_wages = o_hours * o_rate
    totalwages = reg_wages + o_wages
    print( 'Regular hours: ' ,reg_hours, 'Regular Charge: ' , reg_wages)
    print ('Overtime hours:' ,o_hours, 'Overtime Charge: ' , o_wages ) 
    print ('Total wage: ', totalwages)




    pass


if __name__ == '__main__':
    main()
