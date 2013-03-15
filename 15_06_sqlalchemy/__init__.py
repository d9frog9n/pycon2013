#transactions acid model - atomic, consistensy, isolation, durable
#ORM mappers and transactions
#persiting methods - save, delete
#optional trancs - thread.local or autocommit
#python specific - mapped objects is not equal (diffrent instances)
#issues of active record - sql ordering coordination, clear pattern,
#uncommited data can leak to athor trancs
#session solves is
#
#session strategy
#object is row proxy
#lazy flushes
#identity map coordinates row states in memory
