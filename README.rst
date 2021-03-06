===============
 django-pursed
===============

A simple wallet django application

Creating a New Wallet
=====================

A wallet is owned by a user. Should you be using a custom user model,
the wallet should still work properly as it the wallet points to
`settings.AUTH_USER_MODEL`.

.. code-block:: python

   from wallet.models import Wallet

   # wallets are owned by users.
   wallet = user.wallet_set.create()


Despositing a balance to a wallet
=================================

.. code-block:: python

   from django.db import transaction

   with transaction.atomic():
       # We need to lock the wallet first so that we're sure
       # that nobody modifies the wallet at the same time 
       # we're modifying it.
       wallet = Wallet.select_for_update().get(pk=wallet.id)
       wallet.deposit(100)  # amount

Withdrawing a balance from a wallet
===================================

.. code-block:: python

   from django.db import transaction

   with transaction.atomic():
       # We need to lock the wallet first so that we're sure
       # that nobody modifies the wallet at the same time 
       # we're modifying it.
       wallet = Wallet.select_for_update().get(pk=wallet.id)
       wallet.withdraw(100)  # amount

Withdrawing with an insufficient balance
========================================

When a user tries to withdraw from a wallet with an amount greater
than its balance, the transaction raises a
`wallet.errors.InsufficientBalance` error.

.. code-block:: python
                
   # wallet.current_balance  # 50

   # This raises an wallet.errors.InsufficentBalance.
   wallet.withdraw(100)

This error inherits from `django.db.IntegrityError` so that when it is
raised, the whole transaction is automatically rolled-back.

Transferring between wallets
============================

One can transfer a values between wallets. It uses `withdraw` and
`deposit` internally. Should the sending wallet have an insufficient
balance, `wallet.errors.InsufficientBalance` is raised.

.. code-block:: python
                
   with transaction.atomic():
       wallet = Wallet.select_for_update().get(pk=wallet_id)
       transfer_to_wallet = Wallet.select_for_update().get(pk=transfer_to_wallet_id)
       wallet.transfer(transfer_to_wallet, 100)

CURRENCY_STORE_FIELD
====================

The `CURRENCY_STORE_FIELD` is a django field class that contains how
the fields should be stored. By default, it uses
`django.models.BigIntegerField`. It was chosen that way for
simplicity - just make cents into your smallest unit (0.01 -> 1, 1.00
-> 100).

You can change this to decimal by adding this to your settings.py:

.. code-block:: python
                
   # settings.py
   CURRENCY_STORE_FIELD = models.DecimalField(max_digits=10, decimal_places=2)

You need to run `./manage.py makemigrations` after that.
