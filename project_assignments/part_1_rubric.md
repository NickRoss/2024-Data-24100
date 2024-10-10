### Part 1 Rubric Tasklist

## Repository organization
- [ ] Created group on canvas
- [ ] Private repository properly named, invited TA's and instructor
- [ ] Branch protection
- [ ] Used a branch
- [ ] There was a pull request
  - The branch can still exist, but we will take off points in future grading if it is reused.
- [ ] Sent a proper commit hash

## File organization

- [ ] README.md
  - Tells us a little about your group, and the different folders/files
- [ ] DockerFile
  - Has proper instructions to run code and set up proper environment conditions (not too much for this part)
- [ ] requirements.txt
  - Has any and all python/library versions
- [ ] utils folder
  - Your code in this folder
- [ ] data folder
  - Your data in this folder
- [ ] No intermediate files

## Code execution

- [ ] Does it run according to the specs? 
   - Runs with - `docker build . -t data241`, then `docker run -t data241`
   - Returns:
      - Rows in Combined
      - Rows from each market
      - The date at which BRK.A recorded its highest open

## Code quality (rough outline, read instructions for more info)

- [ ] Everything in functions
- [ ] Proper naming conventions for files, functions, variables.
  - We will not test `black` or `flake8`/any linting, just an eye check
- [ ] Descriptive comments if any