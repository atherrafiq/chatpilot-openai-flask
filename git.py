import os
import random
from datetime import datetime, timedelta

# Define the start and end date
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

total_commits = 0
commit_range = (400, 440)  # Adjusted range to ensure a good spread
target_commits = random.randint(*commit_range)

commit_weights = [0.05, 0.15, 0.5, 0.3]  # Adjusted commit probabilities
commit_options = [0, 1, 2, 3]  # Now matches the weights list

dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
random.shuffle(dates)

# Distribute commits over more days by ensuring each commit date has at least 1 commit
commit_distribution = {date: 0 for date in dates}

while total_commits < target_commits:
    for commit_date in dates:
        if total_commits >= target_commits:
            break
        
        commit_count = random.choices(commit_options, weights=commit_weights)[0]
        commit_count = min(commit_count, target_commits - total_commits)

        commit_distribution[commit_date] += commit_count
        total_commits += commit_count

# Perform the commits
for commit_date, commit_count in commit_distribution.items():
    for _ in range(commit_count):
        with open('test.txt', 'a') as file:
            file.write(f'Commit on {commit_date.strftime("%Y-%m-%d %H:%M:%S")}\n')
        
        os.system('git add test.txt')
        commit_message = f'Automated commit on {commit_date.strftime("%Y-%m-%d")}'
        os.system(f'GIT_COMMITTER_DATE="{commit_date}" git commit --date="{commit_date}" -m "{commit_message}"')

        print(f'Committed on {commit_date.strftime("%Y-%m-%d")}')

os.system('git push -u origin main')
print(f'All {total_commits} commits pushed to repository.')
