#Plot of numeric variables, hue=loan status
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 4))

sns.set_style('ticks')
sns.histplot(data=df, x='ApplicantIncome', ax=ax[0], edgecolor='.2', hue='Loan_Status', multiple='stack')
ax[0].set(xlabel='Applicant Income ($)')
ax[0].set_title('Applicant Income Distribution', fontsize=13, fontweight='bold', y=1.05)

sns.histplot(data=df, x='CoapplicantIncome', ax=ax[1], edgecolor='.2', hue='Loan_Status', multiple='stack')
ax[1].set(xlabel='Co-applicant Income ($)')
ax[1].set_title('Co-applicant Income Distribution', fontsize=13, fontweight='bold', y=1.05)

sns.histplot(data=df, x='LoanAmount', ax=ax[2], edgecolor='.2', hue='Loan_Status', multiple='stack')
ax[2].set(xlabel='Loan Amount ($)')
ax[2].set_title('Loan Amount Distribution', fontsize=13, fontweight='bold', y=1.05)

sns.despine()
plt.show()

#boxplot: loan status and loan amount
fig, ax = plt.subplots(figsize=(6,6))

sns.boxplot(x='Loan_Status', y='LoanAmount', data=df, palette='Set3')
plt.xlabel('Loan Status')
plt.ylabel('Loan Amount ($)')
plt.title('Loan Amount of Approved and Disapproved Loans', fontsize=13, fontweight='bold', y=1.05)

sns.despine()
plt.show()

# By Gender
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15,6))

sns.boxplot(x='Gender', y='LoanAmount', data=df, ax=ax[0], palette='Set3', hue='Loan_Status')
ax[0].set(xlabel='Gender', ylabel='Loan Amount ($)')
ax[0].set_title('Loan Amount by Gender', fontsize=13, fontweight='bold', y=1.05)

sns.boxplot(x='Gender', y='ApplicantIncome', data=df, ax=ax[1], palette='Set3', hue='Loan_Status')
ax[1].set(xlabel='Gender', ylabel='Applicant Income ($)')
ax[1].set_title('Applicant Income by Gender', fontsize=13, fontweight='bold', y=1.05)

sns.boxplot(x='Gender', y='CoapplicantIncome', data=df, ax=ax[2], palette='Set3', hue='Loan_Status')
ax[2].set(xlabel='Gender', ylabel='Co-applicant Income ($)')
ax[2].set_title('Co-applicant Income by Gender', fontsize=13, fontweight='bold', y=1.05)

sns.despine()
plt.show()

#By Marriage Status

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15,6))

sns.boxplot(x='Married', y='LoanAmount', data=df, ax=ax[0], palette='Set3', hue='Loan_Status')
ax[0].set(xlabel='Marriage Status', ylabel='Loan Amount ($)')
ax[0].set_title('Loan Amount by Marriage Status', fontsize=13, fontweight='bold', y=1.05)

sns.boxplot(x='Married', y='ApplicantIncome', data=df, ax=ax[1], palette='Set3', hue='Loan_Status')
ax[1].set(xlabel='Marriage Status', ylabel='Applicant Income ($)')
ax[1].set_title('Applicant Income by Marriage Status', fontsize=13, fontweight='bold', y=1.05)

sns.boxplot(x='Married', y='CoapplicantIncome', data=df, ax=ax[2], palette='Set3', hue='Loan_Status')
ax[2].set(xlabel='Marriage Status', ylabel='Co-applicant Income ($)')
ax[2].set_title('Co-applicant Income by Marriage Status', fontsize=13, fontweight='bold', y=1.05)

sns.despine()
plt.show()

#By Education

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15,6))

sns.boxplot(x='Education', y='LoanAmount', data=df, ax=ax[0], palette='Set3', hue='Loan_Status')
ax[0].set(xlabel='Education Status', ylabel='Loan Amount ($)')
ax[0].set_title('Loan Amount by Education Status', fontsize=13, fontweight='bold', y=1.05)

sns.boxplot(x='Education', y='ApplicantIncome', data=df, ax=ax[1], palette='Set3', hue='Loan_Status')
ax[1].set(xlabel='Education Status', ylabel='Applicant Income ($)')
ax[1].set_title('Applicant Income by Education Status', fontsize=13, fontweight='bold', y=1.05)

sns.boxplot(x='Education', y='CoapplicantIncome', data=df, ax=ax[2], palette='Set3', hue='Loan_Status')
ax[2].set(xlabel='Education Status', ylabel='Co-applicant Income ($)')
ax[2].set_title('Co-applicant Income by Education Status', fontsize=13, fontweight='bold', y=1.05)

sns.despine()
plt.show()

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,6))

sns.boxplot(x='Education', y='ApplicantIncome', data=df, palette='Set3', ax=ax[0])
ax[0].set(xlabel='Education Status', ylabel='Applicant Income ($)')
ax[0].set_title('Applicant Income by Education Status', fontsize=13, fontweight='bold', y=1.05)

sns.histplot(data=df, x='ApplicantIncome', palette='Set3', edgecolor='.2', hue='Education', multiple='stack', ax=ax[1])
ax[1].set(xlabel='Application Income')
ax[1].set_title('Applicant Income Distribution by Education Status')
sns.despine()
plt.show()
