#Task1 Q1
'''
GIT WORKFLOW FUNDAMENTALS:
Working Directory:consists of files that you are currently working on, is like your project folder.
Staging Area: is like a rough draft space, it's where you can git add the version of a file or multiple files that you want to save in your next commit (in other words, in the next version of your project).
Local Repo (head): is the current commit your repo is on. Most of the time HEAD points to the latest commit in your current branch, but that doesn't have to be the case.
Remote repo (master): is the name of the default branch that git creates for you when first creating a repo. In most cases, "master" means "the main branch". Most shops have everyone pushing to master, and master is considered the definitive view of the repo.

WORKING DIRECTORY STATES:
Staged: A staging step in git allows you to continue making changes to the working directory, and when you decide you wanna interact with version control, it allows you to record changes in small commits.
Modified: As you edit files, Git sees them as modified, because you've changed them since your last commit.
Committed: Commits can be thought of as snapshots or milestones along the timeline of a Git project. Commits are created with the git commit command to capture the state of a project at that point in time. Git Snapshots are always committed to the local repository.
As you work, you selectively stage these modified files and then commit all those staged changes, and the cycle repeats.

GIT COMMANDS:
Git add: The git add command adds new or changed files in your working directory to the Git staging area. git add is an important command - without it, no git commit would ever do anything.
Git commit: The git commit command captures a snapshot of the project's currently staged changes. Committed snapshots can be thought of as “safe” versions of a project—Git will never change them unless you explicitly ask it to.
Git push: The git push command is used to upload local repository content to a remote repository. Pushing is how you transfer commits from your local repository to a remote repo.
Git fetch: It's the counterpart to git push , but whereas fetching imports commits to local branches, pushing exports commits to remote branches.
Git merge: Merging is Git's way of putting a forked history back together again. The git merge command lets you take the independent lines of development created by git branch and integrate them into a single branch.
Git pull: The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content. Merging remote upstream changes into your local repository is a common task in Git-based collaboration work flows.

'''

#Task2 Q1
#When we want to run the unit tests
'''
account_balance = 100
times_for_pin = [1,2,3]
def right_or_wrong(pin1):
    if pin1 == '123456':
        return True
    elif pin1 != '123456':
        print('Your code is wrong, please try again')
        return False

def you_can_withdrawal(withdraw):
    if withdraw < 100 or withdraw == 100 :
        return True
    else:
        return False

def new_balance(withdrawal):
    result = 100 - withdrawal
    print('Your account balance is', result, 'now')
    return result

for i in times_for_pin:
    pin_number = input('Please type your pin code :')
    if right_or_wrong(pin_number) == True :
        print('Next Step')
        break
    elif i == 3:
        print('You have tried 3 times, please ask the assistant for help.')

if pin_number == '123456':
    cash_withdrawal = int(input('How much money do you want to withdrawal? '))
    try:
        if you_can_withdrawal(cash_withdrawal) == False:
            raise Exception

        new_balance(cash_withdrawal)


    except:
        print('There is an error, please ask the assistant for help.')

    finally:
        print('Thanks for coming to our bank.')
'''

#Task 3
from unittest import TestCase, main
from test_ATM import right_or_wrong, you_can_withdrawal, new_balance


class TestpinnumberFunction(TestCase):
    def pin_number_is_right(self):
        expected = True
        result = right_or_wrong(pin1='123456')
        self.assertEqual(expected, result)
        
    def pin_number_is_wrong(self):
        expected = False
        result = right_or_wrong(pin1='111111')
        self.assertEqual(expected, result)
        
class Testifwecanwithdrawfunction(TestCase):
    def we_can_withdraw(self):
        expected = True
        result = you_can_withdrawal(withdraw = '99')
        self.assertEqual(expected, result)

    def we_cannot_withdraw(self):
        expected = False
        result = you_can_withdrawal(withdraw='103')
        self.assertEqual(expected, result)
        
class Testnewbalancefunction(TestCase):
    def the_rest_of_money(self):
        my_input_withdraw = 40
        expected = 60
        result = new_balance(my_input_withdraw)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()


