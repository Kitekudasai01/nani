computed section:

<!-- welcomeMessage() {
    const accountOwner = this.currentAccount?.owner.split(' ')[0];
    return accountOwner 
      ? `Welcome back, ${accountOwner}!` 
      : 'Log in to get started';
  } -->
<!-- 
  account() {
    return this.currentAccount || null;
  } -->
  <!-- formattedBalance() {
    if (!this.account) return '0€';
  
    const balance = this.calculateBalance();
    return this.formatCurrency(balance);
  }
  
  calculateBalance() {
    return this.account.movements.reduce((acc, mov) => acc + mov, 0);
  } -->
  <!-- sortedMovements() {
    const movements = [...this.account.movements]; // Create a shallow copy of movements
    return this.isSorted ? this.sortMovements(movements) : movements;
  }
  
  sortMovements(movements) {
    return movements.sort((a, b) => a - b);
  } -->

  <!-- formattedIncome() {
    const totalIncome = this.calculateTotalIncome();
    return this.formatCurrency(totalIncome);
  }
  
  calculateTotalIncome() {
    return this.account.movements
      .filter((mov) => mov > 0)
      .reduce((acc, mov) => acc + mov, 0);
  } -->
  <!-- formattedOut() {
    const totalOut = this.calculateTotalOut();
    return this.formatCurrency(totalOut);
  }
  
  calculateTotalOut() {
    const negativeMovements = this.account.movements.filter((mov) => mov < 0);
    return negativeMovements.reduce((acc, mov) => acc + mov, 0);
  } -->
  <!-- formattedInterest() {
    const totalInterest = this.calculateTotalInterest();
    return this.formatCurrency(totalInterest);
  }
  
  calculateTotalInterest() {
    return this.account.movements
      .filter((mov) => mov > 0)
      .map((deposit) => this.calculateInterest(deposit))
      .reduce((acc, interest) => acc + interest, 0);
  }
  
  calculateInterest(deposit) {
    return (deposit * this.account.interestRate) / 100;
  }
   -->

   <!-- formattedDate() {
    const currentDate = new Date();
    return this.formatDate(currentDate);
  }
  
  formatDate(date) {
    return new Intl.DateTimeFormat(this.account.locale, {
      day: 'numeric',
      month: 'long',
      year: 'numeric',
    }).format(date);
  } -->
  
  <!-- formattedTimer() {
    const minutes = this.formatTimeUnit(Math.floor(this.timeRemaining / 60));
    const seconds = this.formatTimeUnit(this.timeRemaining % 60);
    return `${minutes}:${seconds}`;
  }
  
  formatTimeUnit(unit) {
    return String(unit).padStart(2, '0');
  } -->

  <!-- currentBalance() {
    return this.calculateBalance(this.currentAccount.movements);
  }
  
  calculateBalance(movements) {
    return movements.reduce((acc, mov) => acc + mov, 0);
  } -->

method section:

<!-- handleLogin() {
    const account = this.findAccountByOwnerInitials(this.loginUser);
    
    if (this.isValidAccount(account, this.loginPin)) {
      this.currentAccount = account;
      this.startLogOutTimer();
    } else {
      alert('Invalid login credentials');
    }
  }
  
  findAccountByOwnerInitials(loginUser) {
    return this.accounts.find((acc) => this.getOwnerInitials(acc.owner) === loginUser);
  }
  
  getOwnerInitials(owner) {
    return owner.toLowerCase().split(' ').map(name => name[0]).join('');
  }
  
  isValidAccount(account, loginPin) {
    return account?.pin === +loginPin;
  } -->
  
  <!-- movementType(movement) {
    return movement > 0 ? this.getDepositClass() : this.getWithdrawalClass();
  }
  
  getDepositClass() {
    return 'movements__type--deposit';
  }
  
  getWithdrawalClass() {
    return 'movements__type--withdrawal';
  } -->

  <!-- formatMovementDate(dateString) {
    const date = new Date(dateString);
    const daysPassed = this.calculateDaysPassed(date);
  
    return this.formatDateBasedOnDays(daysPassed, date);
  }
  
  calculateDaysPassed(date) {
    return Math.floor((new Date() - date) / (1000 * 60 * 60 * 24));
  }
  
  formatDateBasedOnDays(daysPassed, date) {
    if (daysPassed === 0) return 'Today';
    if (daysPassed === 1) return 'Yesterday';
    return daysPassed <= 7
      ? `${daysPassed} days ago`
      : new Intl.DateTimeFormat(this.account.locale).format(date);
  } -->
  
  <!-- formatCurrency(value) {
    return this.createCurrencyFormatter().format(value);
  }
  
  createCurrencyFormatter() {
    return new Intl.NumberFormat(this.account.locale, {
      style: 'currency',
      currency: this.account.currency,
    });
  } -->
  
  <!-- sortMovements() {
    this.toggleSortOrder();
  }
  
  toggleSortOrder() {
    this.isSorted = !this.isSorted;
  }
  
  startLogOutTimer() {
    this.clearExistingTimer();
    this.resetTimer();
    this.timer = setInterval(() => this.updateTimer(), 1000);
  }
  
  clearExistingTimer() {
    if (this.timer) clearInterval(this.timer);
  }
  
  resetTimer() {
    this.timeRemaining = 300;
  }
  
  updateTimer() {
    this.timeRemaining--;
    if (this.timeRemaining === 0) {
      this.endSession();
    }
  }
  
  endSession() {
    clearInterval(this.timer);
    this.currentAccount = null;
  }
   -->
<!-- 
   transferMoney() {
    const receiverAcc = this.findAccountByInitials(this.transferTo);
  
    if (this.isTransferValid(receiverAcc)) {
      this.executeTransfer(receiverAcc);
      this.resetTransferFields();
      this.updateUI();
      alert('Transfer successful');
    } else {
      alert('Invalid transfer details. Please input correct username and amount.');
    }
  }
  
  findAccountByInitials(initials) {
    return this.accounts.find((acc) => this.getOwnerInitials(acc.owner) === initials);
  }
  
  isTransferValid(receiverAcc) {
    return (
      receiverAcc &&
      this.transferAmount > 0 &&
      this.currentBalance >= this.transferAmount && // using computed balance here
      receiverAcc !== this.currentAccount // prevent transferring to self
    );
  }
  
  executeTransfer(receiverAcc) {
    this.currentAccount.movements.push(-this.transferAmount);
    receiverAcc.movements.push(this.transferAmount);
    const timestamp = new Date().toISOString();
    this.currentAccount.movementsDates.push(timestamp);
    receiverAcc.movementsDates.push(timestamp);
  }
  
  resetTransferFields() {
    this.transferAmount = 0;
    this.transferTo = '';
  } -->
  
  <!-- requestLoan() {
    if (this.isLoanRequestValid()) {
      this.processLoanApproval();
    } else {
      alert('Loan request denied');
    }
  }
  
  isLoanRequestValid() {
    return (
      this.loanAmount > 0 &&
      this.currentAccount.movements.some((mov) => mov >= this.getMinimumLoanRequirement())
    );
  }
  
  getMinimumLoanRequirement() {
    return (this.loanAmount * 10) / 100;
  }
  
  processLoanApproval() {
    setTimeout(() => {
      this.currentAccount.movements.push(this.loanAmount);
      this.currentAccount.movementsDates.push(new Date().toISOString());
      this.resetLoanFields();
      this.updateUI();
      alert('Loan approved');
    }, 2000);
  }
  
  resetLoanFields() {
    this.loanAmount = 0;
  } -->

  <!-- closeAccount() {
    if (this.isCloseAccountValid()) {
      this.removeAccount();
      this.resetLoginFields();
      alert('Account closed');
    } else {
      alert('Incorrect details');
    }
  }
  
  isCloseAccountValid() {
    return (
      this.closeUser === this.loginUser &&
      +this.closePin === this.currentAccount.pin
    );
  }
  
  removeAccount() {
    const index = this.accounts.findIndex(
      (acc) => acc.username === this.currentAccount.username
    );
    if (index !== -1) {
      this.accounts.splice(index, 1);
      this.currentAccount = null;
    }
  }
  
  resetLoginFields() {
    this.loginUser = '';
    this.loginPin = '';
  } -->
<!-- 
  updateUI() {
    this.triggerUIUpdate();
  }
  
  triggerUIUpdate() {
    this.$forceUpdate(); // Forces the UI to re-render after updates
  } -->
  
  
  
  
  
  
  
  
  
  
  