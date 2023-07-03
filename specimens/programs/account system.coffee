\ account system


spec code { ver = 5.6 | syn = utinax | sty = stan }

create struct 'account' {
  evolve account.create(ctx) [
    | str 'username'
    | str 'password'
    | int 'lockout' = 3
  ] {
    account.autoset(username, password, lockout)
    set account.'state' = false
    set account.'attempts' = 0
    set account.'log' = (("created", datix.now()))
  }

  define account.'login'(password) {
    if password = account.password {
      set account.state = true
      add "login success", datix.now() to account.log
    else |
      alt account.attempts + 1
      if account.attempts > account.lock {
        add "account locked", datix.now() to account.log
        evoke ...
      else |
      add "failed login attempt", datix.now() to account.log
        evoke ...
      }
    }
  }

  define account.'logout'() {
    set account.state = false
    add "manual logout" to account.log
  }
}


on start loop forever {{
  ...
}}
