# Oozie REPL

## Export ENV variables

```
$ export OOZIE_HOST="<host>"
$ export HISTORY_SERVER="<host>"
```

## Simple print

```
$ ./repl.py

In [1]: p(all())
RUNNING ---> sello-product-view-facts                           Sat, 23 Apr 2016 11:19:00 EST by oozie
RUNNING ---> reportify-rdb-funnels-daily-rollup                 Sat, 23 Apr 2016 11:18:25 EST by oozie
RUNNING ---> reportify-rdb-browsers-daily-rollup                Sat, 23 Apr 2016 11:16:02 EST by oozie
RUNNING ---> smileys-facts                                      Sat, 23 Apr 2016 11:15:19 EST by oozie
SUCCEEDED -> storefront-session-dimless-rollup-resolver-v2      Sat, 23 Apr 2016 11:14:34 EST by oozie

In [2]: p(all(n=10))
RUNNING ---> sello-product-view-facts                           Sat, 23 Apr 2016 11:19:00 EST by oozie
RUNNING ---> reportify-rdb-funnels-daily-rollup                 Sat, 23 Apr 2016 11:18:25 EST by oozie
RUNNING ---> reportify-rdb-browsers-daily-rollup                Sat, 23 Apr 2016 11:16:02 EST by oozie
RUNNING ---> smileys-facts                                      Sat, 23 Apr 2016 11:15:19 EST by oozie
SUCCEEDED -> storefront-session-dimless-rollup-resolver-v2      Sat, 23 Apr 2016 11:14:34 EST by oozie
SUCCEEDED -> storefront-session-referrer-rollup-resolver-v2     Sat, 23 Apr 2016 11:14:34 EST by oozie
RUNNING ---> referrer-domain-metrics-accumulating-resolver-v... Sat, 23 Apr 2016 11:14:34 EST by oozie
RUNNING ---> referrer-path-metrics-accumulating-resolver-v2     Sat, 23 Apr 2016 11:14:34 EST by oozie
RUNNING ---> reportify-rdb-devices-daily-rollup                 Sat, 23 Apr 2016 11:10:02 EST by oozie
SUCCEEDED -> theme-dimension                                    Sat, 23 Apr 2016 11:09:00 EST by oozie
```

## Detailed print

```
$ ./repl.py

In [1]: pp(all())
RUNNING ---> sello-product-view-facts                           Sat, 23 Apr 2016 11:19:00 EST by oozie
  OK --------> build                                              11:19:00 to 11:23:25
  OK --------> resolve                                            11:23:25 to 11:23:48
  RUNNING ---> redshift-load                                      11:23:48 to --:--:--
  RUNNING ---> mysql-analytics_aurora-load                        11:23:49 to --:--:--
  RUNNING ---> hive-load                                          11:23:50 to --:--:--
  RUNNING ---> mysql-reportify_usw2-load                          11:23:51 to --:--:--

RUNNING ---> reportify-rdb-funnels-daily-rollup                 Sat, 23 Apr 2016 11:18:25 EST by oozie
  RUNNING ---> build                                              11:18:25 to --:--:--

RUNNING ---> reportify-rdb-browsers-daily-rollup                Sat, 23 Apr 2016 11:16:02 EST by oozie
  RUNNING ---> build                                              11:16:02 to --:--:--

RUNNING ---> smileys-facts                                      Sat, 23 Apr 2016 11:15:19 EST by oozie
  OK --------> build                                              11:15:19 to 11:15:43
  RUNNING ---> resolve                                            11:15:43 to --:--:--

SUCCEEDED -> storefront-session-dimless-rollup-resolver-v2      Sat, 23 Apr 2016 11:14:34 EST by oozie
  OK --------> resolve                                            11:14:34 to 11:15:04
```

## Detailed print of recently failed jobs

```
$ ./repl.py

In [1]: pp(failed(n=2))
FAILED ----> create-parquet-tables                              Tue, 19 Apr 2016 18:12:00 EST by oozie
  KILLED ----> shopify_a_h                                        18:12:00 to 18:13:20
  KILLED ----> shopify_remainder                                  18:12:01 to 18:13:18
  KILLED ----> frontroom                                          18:12:02 to 18:13:08
  KILLED ----> shopify_i_o                                        18:12:03 to 18:13:11
  KILLED ----> sensitive                                          18:12:03 to 18:13:20
  ERROR -----> shopify_p                                          18:12:04 to 18:13:07
  KILLED ----> other_remainder                                    18:12:05 to 18:13:15
  KILLED ----> other_a_e                                          18:12:06 to 18:13:20
  ERROR -----> other_f_q                                          18:12:06 to 18:13:04

FAILED ----> zendesk-ticket-pipeline-facts                      Fri, 08 Apr 2016 22:49:16 EST by oozie
  KILLED ----> interaction-facts                                  22:49:16 to 23:14:42
    SUCCEEDED -> forum-post-facts                                 22:49:17 to 22:52:21
      OK --------> build                                          22:49:17 to 22:49:45
      OK --------> resolve                                        22:49:46 to 22:50:15
      OK --------> redshift-load                                  22:50:15 to 22:52:21
      OK --------> hive-load                                      22:50:16 to 22:50:52
    KILLED ----> zendesk-ticket-pipeline-prebuild                 22:49:17 to 23:08:48
      KILLED ----> zendesk-ticket-comment-facts                   22:49:17 to 23:08:48
        OK --------> build                                        22:49:17 to 23:00:57
        OK --------> resolve                                      23:00:57 to 23:07:31
        ERROR -----> redshift-load                                23:07:31 to 23:08:46
        OK --------> hive-load                                    23:07:32 to 23:08:48
    SUCCEEDED -> phone-call-facts                                 22:49:17 to 23:14:42
      OK --------> build                                          22:49:17 to 23:00:46
      OK --------> resolve                                        23:00:47 to 23:11:18
      OK --------> redshift-load                                  23:11:18 to 23:14:42
      OK --------> hive-load                                      23:11:19 to 23:11:56
  KILLED ----> outbound-phone-call-facts                          22:49:17 to 23:05:20
    OK --------> build                                            22:49:17 to 23:00:32
    OK --------> resolve                                          23:00:32 to 23:04:03
    ERROR -----> redshift-load                                    23:04:03 to 23:05:19
    OK --------> hive-load                                        23:04:04 to 23:04:45
```

## Detailed print by job name

```
$ OOZIE_HOST="<host>" ./repl.py

In [1]: pp(by_name('smileys-facts', n=2))
RUNNING ---> smileys-facts                                      Sat, 23 Apr 2016 11:15:19 EST by oozie
  OK --------> build                                              11:15:19 to 11:15:43
  RUNNING ---> resolve                                            11:15:43 to --:--:--

SUCCEEDED -> smileys-facts                                      Sat, 23 Apr 2016 07:41:22 EST by oozie
  OK --------> build                                              07:41:22 to 07:43:50
  OK --------> resolve                                            07:43:50 to 07:44:30
  OK --------> redshift-load                                      07:44:30 to 08:14:28
  OK --------> hive-load                                          07:44:31 to 07:46:06
```

## Include logs in detailed print

```
$ ./repl.py

In [1]: pp(all(n=1), logs=True)
RUNNING ---> product-label-metadata                             Tue, 26 Apr 2016 20:57:00 EST by oozie
  RUNNING ---> build                                              20:57:00 to --:--:--
               <host>/node/containerlogs/container_e04_145522548_352939_01_000001/oozie/stdout/?start=0
```

## Generate and open flow graph

```
$ ./repl.py

In [1]: flow = by_name('smileys-facts', n=1)[0]

In [2]: open_graph(flow)
```
