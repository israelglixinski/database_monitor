# database_monitor

### Oracle

* 1 - Configure .env (já está usando):
```
ORACLE_HOST=127.0.0.1
ORACLE_PORT=1521
ORACLE_BASE=XE
ORACLE_USER=meu_usuario
ORACLE_PASS=minha_senha
```

* 2 - Crie o cenário e dados de base:
```
python oracle.py init --seed-products 2000 --seed-customers 20000
```

* 3 - Rode carga por 5 minutos com 8 threads e lote de 2k inserts por rodada:
```
python oracle.py workload --minutes 5 --workers 8 --insert-batch 2000 --mix 0.6,0.3,0.1
```

* 4 - Em paralelo (ou antes/depois), monitore por 90s tirando snapshot a cada 2s:
```
python oracle.py monitor --seconds 90 --every 2
```

* OBS - Se o monitor acusar falta de privilégio nas v$ views, peça ao DBA (ambiente de teste!) algo como:
```
GRANT SELECT_CATALOG_ROLE TO MEU_USUARIO;
-- ou permissões pontuais, por exemplo:
GRANT SELECT ON V_$SESSION TO MEU_USUARIO;
GRANT SELECT ON V_$SQLAREA TO MEU_USUARIO;
GRANT SELECT ON V_$SEGMENT_STATISTICS TO MEU_USUARIO;
```

