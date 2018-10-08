"""
    This program is to simulate a task of hiring an assistant
"""

def interview(A,best):  # advices if the current guy is better than best or not
    if(A>=best):
        return True
    else:
        return False


def Hire_assistant(A,cost_interview,cost_hiring): # method for hiring
    size = len(A)
    candidates_hired = []
    total_interview_cost = 0 #cost incurred to be paid for interviewing body
    total_hiring_cost =0 #cost incurred for hiring
    best = 0 #candidate least qualified for getting hired
    
    for i in range(size):
        cand_selected = interview(A[i],best)
        total_interview_cost = total_interview_cost+cost_interview
        
        if(cand_selected):
            best = candidates[i]
            candidates_hired.append(i)
            total_hiring_cost = total_hiring_cost+cost_hiring
    
    print "\n hired candidates are - ",candidates_hired,"\n"
    print "\n Interview cost = ",total_interview_cost
    print "\nHiring cost =",total_hiring_cost,"\n"
    

try:
    print "\n Enter the list of candidates in the order of priority to be hired\n"
    
    candidates = [int(x) for x in raw_input().split()]
    
    cost_interview = int(raw_input("\n Enter the cost of interviewing a candidate\n"))
    
    cost_hiring = int(raw_input("\n Enter the cost of hiring a candidate\n"))
    
    if (cost_hiring < cost_interview):
        print "\n Interview cost cannot be lesser than Hiring cost\n"
        exit(0)
    
    Hire_assistant(candidates,cost_interview,cost_hiring)
    
except ValueError:
    print " \nERROR: INVALID INPUT\n"
    exit(1)