# CLI's for load testing

## Table of Contents

* [wrk](#wrk)
  * [wrk install](#wrk-install)
  * [wrk run](#wrk-run)
* [ab (Apache Bench)](#ab-apache-bench)
  * [ab run](#ab-run)
* [siege](#siege)
  * [siege install](#siege-install)
  * [siege run](#siege-run)
* [hey](#hey)
  * [hey install](#hey-install)
  * [hey run](#hey-run)
* [locust](#locust)
  * [locust install](#locust-install)
  * [locust run](#locust-run)
* [k6](#k6)
  * [k6 install](#k6-install)
  * [k6 run](#k6-run)
* [Install all](#install-all)
* [Run all](#run-all)

## [wrk](https://github.com/wg/wrk)

### wrk install

```sh
brew install wrk
```

### wrk run

```sh
wrk -t12 -c400 -d30 --latency --timeout 2s <URL>
```

## [ab (Apache Bench)](https://httpd.apache.org/docs/2.4/programs/ab.html)

### ab run

```sh
ab -n 400 -c 100 -s 2 -t 30 -k <URL>
```

## [siege](https://github.com/JoeDog/siege)

### siege install

```sh
brew install siege
```

### siege run

```sh
siege -b -r 10 -c 40 <URL>
```

## [hey](https://github.com/rakyll/hey)

### hey install

```sh
brew install hey
```

### hey run

```sh
hey -n 400 -c 100 -t 2 <URL>
```

## [locust](https://locust.io/)

### locust install

```sh
brew install locust
```

### locust run

```sh
locust -f locust/locustfile.py --headless --users 10 --spawn-rate 1 -H <URL>
```

## [k6](https://k6.io/docs/getting-started/running-k6/)

### k6 install

```sh
brew install k6
```

### k6 run

```sh
k6
```

## Install all

```sh
brew install wrk siege hey locust k6
```

## Run all

```sh
wrk -t12 -c400 -d30  --timeout 2s --latency <URL>
ab -n 400 -c 100 -s 2 -t 30 -k <URL>
siege -b -r 10 -c 40 <URL>
hey -n 400 -c 100 -t 2 <URL>
locust -f locust/locustfile.py --headless --users 10 --spawn-rate 1 -H <URL>
```
