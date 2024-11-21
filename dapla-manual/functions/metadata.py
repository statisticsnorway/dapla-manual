import subprocess
from datetime import datetime
import os

def get_last_modified(file_path, suppress_author=False, folder = 'statistikkere'):
    """
    Returns the author and date of the last modified commit.
    If the current date matches the specified implementation date,
    it returns details from the second-last commit; otherwise, it returns
    details from the most recent commit.
    
    Args:
        file_path (str): Name of the given file, including its path. 
                         Eg. "navnestandard.qmd"
        suppress_author (bool): If True, omits the author name in the output.
        folder (bool): Defaults to 'statistikkere' because environemnt is here

    Returns:
        str: A formatted string with the author and date of the relevant commit,
             or an error message if the file or commit log is not found.
    """
    # Define the implementation date for checking
    implementation_date = datetime(2024, 11, 21).date()

    try:
        # Check if the file is tracked by Git
        base_directory = os.path.abspath(os.path.join(os.getcwd(), ".."))
        target_directory = os.path.join(base_directory, folder)
        subprocess.check_output(["git", "ls-files", "--error-unmatch", file_path], stderr=subprocess.DEVNULL, cwd=target_directory)
        
        # Get the last two commits for the specified file
        last_two_commits = subprocess.check_output(
            ["git", "log", "-2", "--pretty=format:%an|%ad", "--date=short", file_path],
            text=True, encoding="utf-8", cwd = target_directory
        ).strip().split('\n')
        
        if not last_two_commits:
            return ""
        
        # Default to the most recent commit
        commit_info = last_two_commits[0]
        
        # If today is the implementation date and there are at least two commits, select the second-last commit
        if datetime.now().date() == implementation_date and len(last_two_commits) > 1:
            commit_info = last_two_commits[1]
        
        # Extract author and date from the commit info
        if suppress_author:
            # Only display the date
            _, date = commit_info.split('|')
            return f"Sist endret: {date}"
        else:
            # Display both author and date
            author, date = commit_info.split('|')
            return f"Sist endret: {date} av {author}"
    
    except subprocess.CalledProcessError:
        return ""