import base64
import os
from time import sleep

# ignore this, scroll down
# ----------------------------
keyCrypt = "YWVzX2tla19nZW5lcmF0aW9uX3NvdXJjZSA9IDRkODcwOTg2YzQ1ZDIwNzIyZmJhMTA1M2RhOTJlOGE5CmFlc19rZXlfZ2VuZXJhdGlvbl9zb3VyY2UgPSA4OTYxNWVlMDVjMzFiNjgwNWZlNThmM2RhMjRmN2FhOApiaXNfa2VrX3NvdXJjZSA9IDM0YzFhMGM0ODI1OGY4YjRmYTllNWU2YWRhZmM3ZTRmCmJpc19rZXlfMDAgPSAzNzRlMGUyYWIyNzUxNDFmODExYmFkY2IwZmVmZDg4MWI3MWQ2YWY1NDBkZTU4ODk1OTAxYWEwYzAxNjYzYmM4CmJpc19rZXlfMDEgPSAwYjA4ZjE5YTQyYWM1YWU1OTBiMzM3M2FkOTY5ODM0NGE1NzFmMzUxNjU2NjM1MzZkYWUwODQyYjUyMjFiMzFjCmJpc19rZXlfMDIgPSAzOGYwOTM2ZjMzYmFjZWRjMGMwYTE1OWZmYmJlZWUwZjQwYmIwODM4NjkxNWJkZDBjNjczMDM0OWI5OTA4MWVjCmJpc19rZXlfMDMgPSAzOGYwOTM2ZjMzYmFjZWRjMGMwYTE1OWZmYmJlZWUwZjQwYmIwODM4NjkxNWJkZDBjNjczMDM0OWI5OTA4MWVjCmJpc19rZXlfc291cmNlXzAwID0gZjgzZjM4NmUyY2QyY2EzMmE4OWFiOWFhMjliZmM3NDg3ZDkyYjAzYWE4YmZkZWUxYTc0YzNiNmUzNWNiNzEwNgpiaXNfa2V5X3NvdXJjZV8wMSA9IDQxMDAzMDQ5ZGRjY2MwNjU2NDdhN2ViNDFlZWQ5YzVmNDQ0MjRlZGFiNDlkZmNkOTg3NzcyNDlhZGM5ZjdjYTQKYmlzX2tleV9zb3VyY2VfMDIgPSA1MmMyZTllYjA5ZTNlZTI5MzJhMTBjMWZiNmEwOTI2YzRkMTJlMTRiMmE0NzRjMWMwOWNiMDM1OWYwMTVmNGU0CmRldmljZV9rZXkgPSBiZDE2YzQ1YjI2NDdkODQyYzVlZTNjODY5ZTNhOTYwNwpkZXZpY2Vfa2V5XzR4ID0gMjA3ODkwMGM2YmIzNmZmZjFmZGFkNTdhN2RkMWI2NmUKZXRpY2tldF9yc2Ffa2VrID0gMTljOGI0NDFkMzE4ODAyYmFkNjNhNWJlZGEyODNhODQKZXRpY2tldF9yc2Ffa2VrX3NvdXJjZSA9IGRiYTQ1MTEyNGNhMGE5ODM2ODE0ZjVlZDk1ZTMxMjViCmV0aWNrZXRfcnNhX2tla2VrX3NvdXJjZSA9IDQ2NmU1N2I3NGE0NDdmMDJmMzIxY2RlNThmMmY1NTM1CmhlYWRlcl9rZWtfc291cmNlID0gMWYxMjkxM2E0YWNiZjAwZDRjZGUzYWY2ZDUyMzg4MmEKaGVhZGVyX2tleSA9IGFlYWFiMWNhMDhhZGY5YmVmMTI5OTFmMzY5ZTNjNTY3ZDY4ODFlNGU0YTZhNDdhNTFmNmU0ODc3MDYyZDU0MmQKaGVhZGVyX2tleV9zb3VyY2UgPSA1YTNlZDg0ZmRlYzBkODI2MzFmN2UyNWQxOTdiZjVkMDFjOWI3YmZhZjYyODE4M2Q3MWY2NGQ3M2YxNTBiOWQyCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wMCA9IGVmOTc5ZTI4OWExMzJjMjNkMzljNGVjNWEwYmJhOTY5CmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wMSA9IGNkZWRiYWI5N2I2OTcyOTA3M2RmYjI0NDBiZmYyYzEzCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wMiA9IDc1NzE2ZWQzYjUyNGEwMWRmZTIxNDU2Y2UyNmM3MjcwCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wMyA9IGY0MjgzMDY1NDRjZjU3MDdjMjVlYWE4YmMwNTgzZmQxCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wNCA9IDc5ODg0NGVjMDk5ZWI2YTA0YjI2YzdjNzI4YTM1YTRkCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wNSA9IGE1N2M2ZWVjYzU0MTBhZGEyMjcxMmViM2NjYmY0NWYxCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wNiA9IDJhNjBmNmM0Mjc1ZGYxNzcwNjUxZDU4OTFiOGU3M2VjCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wNyA9IDMyMjIxYmQ2ZWQxOWI5MzhiZWMwNmI5ZDM2ZWQ5ZTUxCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wOCA9IGZiMjBhYTllM2RiZjY3MzUwZTg2NDc5ZWI0MzFhMGIzCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wOSA9IGNlOGQ1ZmE3OWUyMjBkNWY0ODQ3MGU5ZjIxYmUwMThiCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wYSA9IDM4Yjg2NTcyNWFkY2Y1NjhhODFkMmRiM2NlYWE1YmNjCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wYiA9IGJiZGRmZDQwYTU5ZDBmZjU1NWMwOTU0MjM5OTcyMjEzCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wYyA9IDNmZWU3MjA0ZTIxYzZiMGZmMTM3MzIyNmMwYzNlMDU1CmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl8wZCA9IDdiMDVkMjE0ZmE1NTRiYzNlOTFiMDQ0ZmI0MTJmYzBkCmtleV9hcmVhX2tleV9hcHBsaWNhdGlvbl9zb3VyY2UgPSA3ZjU5OTcxZTYyOWYzNmExMzA5ODA2NmYyMTQ0YzMwZAprZXlfYXJlYV9rZXlfb2NlYW5fMDAgPSBiMzM4MTNlNGM5YzQzOTljNzVmYWJjNjczYWI0OTQ3YgprZXlfYXJlYV9rZXlfb2NlYW5fMDEgPSBjNTQxNjZlZmE4YzljMGY2NTExZmE4YjU4MDE5MTY3NwprZXlfYXJlYV9rZXlfb2NlYW5fMDIgPSAzMDYxY2U3MzQ2MWUwYjA0MDlkNmEzM2RhODU4NDNjOAprZXlfYXJlYV9rZXlfb2NlYW5fMDMgPSAwNmYxNzAwMjVhNjQ5MjFjODQ5ZGYxNjhlNzRkMzdmMgprZXlfYXJlYV9rZXlfb2NlYW5fMDQgPSBkYzg1N2ZkNmRjMWM2MjEzMDc2ZWM3YjkwMmVjNWJiNgprZXlfYXJlYV9rZXlfb2NlYW5fMDUgPSAxMzFkNzZiNzBiZDhhNjAwMzZkODIxOGMxNWNiNjEwZgprZXlfYXJlYV9rZXlfb2NlYW5fMDYgPSAxN2Q1NjU0OTJiYTgxOWIwYzE5YmVkMWI0Mjk3YjY1OQprZXlfYXJlYV9rZXlfb2NlYW5fMDcgPSAzNzI1NTE4NmY3Njc4MzI0YmYyYjJkNzczZWEyYzQxMgprZXlfYXJlYV9rZXlfb2NlYW5fMDggPSA0MTE1YzExOWI3YmQ4NTIyYWQ2M2M4MzFiNmM4MTZhNgprZXlfYXJlYV9rZXlfb2NlYW5fMDkgPSA3OTJiZmM2NTI4NzBjY2E3NDkxZDE2ODUzODRiZTE0NwprZXlfYXJlYV9rZXlfb2NlYW5fMGEgPSBkZmNjOWU4N2U2MWM5ZmJhNTRhOWIxYzI2MmQ0MWU0ZAprZXlfYXJlYV9rZXlfb2NlYW5fMGIgPSA2NmZlMzEwN2Y1YTZhOGQ4ZWRhMjQ1OWQ5MjBiMDdhMQprZXlfYXJlYV9rZXlfb2NlYW5fMGMgPSBiNzliNmJmM2Q2Y2RjNWVjMTAyNzdmYzA3YTRmZWM5MwprZXlfYXJlYV9rZXlfb2NlYW5fMGQgPSA5YTIwZmZiZGNiMDNjZmM1YjhlODhiMDU4ZDI3YWU2YwprZXlfYXJlYV9rZXlfb2NlYW5fc291cmNlID0gMzI3ZDM2MDg1YWQxNzU4ZGFiNGU2ZmJhYTU1NWQ4ODIKa2V5X2FyZWFfa2V5X3N5c3RlbV8wMCA9IDZkZDAyYWExNWI0NDBkNjIzMTIzNmI2Njc3ZGU4NmJjCmtleV9hcmVhX2tleV9zeXN0ZW1fMDEgPSA0YWIxNTVlN2YyOWEyOTIwMzdmZDE0NzU5Mjc3MGIxMgprZXlfYXJlYV9rZXlfc3lzdGVtXzAyID0gYjdhNzRhZGVhZjg5YzJhMTk4YzMyN2JkZmYzMjJkN2QKa2V5X2FyZWFfa2V5X3N5c3RlbV8wMyA9IGQ1YWFiMWFjZDIzYThhZWMyODRhMzE2ZGY4NTlkMzc3CmtleV9hcmVhX2tleV9zeXN0ZW1fMDQgPSA5YjQ0YjQ1YjM3ZGU5ZDE0NzU0YjFkMjJjMmNhNzQyYwprZXlfYXJlYV9rZXlfc3lzdGVtXzA1ID0gMDAxMmU5NTc1MzBkM2RjN2FmMzRmYmJlNmZkNDQ1NTkKa2V5X2FyZWFfa2V5X3N5c3RlbV8wNiA9IDAxNzQ0ZTNiMDgxODQ0NWNkNTRlZTlmODlkYTQzMTkyCmtleV9hcmVhX2tleV9zeXN0ZW1fMDcgPSBkMGQzMGU0NmY1Njk1Yjg3NWYxMTUyMmMzNzVjNWE4MAprZXlfYXJlYV9rZXlfc3lzdGVtXzA4ID0gYmQwNmNiMWI4NmJkNWM0MzM2Njc0NzBhMDllYjYzZGUKa2V5X2FyZWFfa2V5X3N5c3RlbV8wOSA9IGUxOWY3ODhmNjU4ZWRhOGJiZjM0YTFkZDJhOTUwM2E5CmtleV9hcmVhX2tleV9zeXN0ZW1fMGEgPSA3MDcwZTdmZjVjZmU0NDg2MzAxNDNhOTg3NDkwM2MzOAprZXlfYXJlYV9rZXlfc3lzdGVtXzBiID0gM2ZhNDcxZDQ0ODNlNThiOGY3NzU2ZmNiNjRmNjM4OTAKa2V5X2FyZWFfa2V5X3N5c3RlbV8wYyA9IDdiZmQzODFkZjMzNjk0MDdhYjFjNmJkZDlmYWJmNTIyCmtleV9hcmVhX2tleV9zeXN0ZW1fMGQgPSA1M2VkNTMxY2Q2NTdlZGY0NDNiNTUxYTk2NGY0NGVjYwprZXlfYXJlYV9rZXlfc3lzdGVtX3NvdXJjZSA9IDg3NDVmMWJiYTZiZTc5NjQ3ZDA0OGJhNjdiNWZkYTRhCmtleWJsb2JfMDAgPSBmNzU5MDI0ZjgxOTkxMDFkZGRjMWVmOTFlNmVlY2YzN2UyNGI5NWFjOTI3MmY3YWU0NDFkNWQ4MDYwYzg0M2E0ODMyMmQyMWNkZDA2ZDRmYzk1OGM2OGQzODAwZWI0ZGI5MzlmZmJlYzkzMDE3N2Y3N2QxMzYxNDRmZjYxNWFhODgzNWU4MTFiYjk1OGRlZGEyMThmODQ4NmI1YTEwZjUzMWIzMGNiOWQyNjk2NDVhYzlmYzI1YzUzZmM4MDUyNWU1NmJkMzYwMjk4OGE5ZmNmMDZiYmY5OWNhOTEwYWQ2NTMwNzkxZDUxMmM5ZDU3ZTE3YWJmNDkyMjBkZTY0MTliZjRlY2ExNjg1YzFlNGRmNzdmMTlkYjdiNDRhOTg1Y2EKa2V5YmxvYl8wMSA9IGJkMjcyNjRhZTA3ZTk3OTc1NjQxMWQwYzY2ZTY3OWUzYzUwODUxZjNlOTAyZDljMmNkMWE0MzhiOTQ4MTU5YTUxN2VjMTU2NmMxMDU3MDMyNmVhMjY5N2VlNjJkYTQ2ZjE0YmI1ZDU4MWJmYzA2ZmQwYzkzODdlYTMzZDJkNGRjNjNlNzgwOWJhOTBmMDNkZDJjNzExMmZmYmZhNTQ4OTUxYjliOGM2ODhiNWU0ZjI5NTFkMjRhNzNkYTI5YzY2ODE1NGE1ZDQ4MzhkYmE3MWVlMDY4YWNlODNmZTcyMGU4YzJhNDk1YzU5NmY3MzUyNWRjM2MwNTk5NGI0MGFkMjdmOGM2MDMyMmY3NWNkNTQ4YjgyMWFmOTE2MmUxNmY3NgprZXlibG9iXzAyID0gYTNkNGE4ZTE1M2I4ZTZhZTZlNmFlZjNlOGYyMTljYjRiNzc5MGY0Nzg1NmFjY2M3NjI2OGY5YWZhOTlhMWZmOGIxYTcyZjYzZDFmOTlmNDgwYTNjMTUzMjA3OGJiNTlhYmRkMjUyMDNjZmIxMmEzOGIzM2U5YmE2YTA5YWZiNmYyNDI4M2IzYmE3NmEwMTYxMjMwYTczNjY5ZGRmNTQ5M2MyYjc5MTlkMDk0ZmQ3OTViNDg0Nzk0ODU0ZjcxZTRmNGM2NzIyNDVkNzc3MGUyOTM5NzcyMjQ0NGQxMTFiNDIyOWNkYmYzNTcwN2I3MDYzNGVhOGYxNDA3NjZlODg0Y2M1ODBjYjFlMmQ5YWE5ODY2ZmZlZjkyMDAxMGZjNDA5CmtleWJsb2JfMDMgPSAxNTU4ZjUyNWFlOGM1YmU5MjQzZmI2ZDhhOGIwYThlZTBlODg2YTU5MDM1NjY4NzQwYTkzNjYxOWI3YTVjODNlODIxMTk4YjE3MWQxOGU1MTQ0NTA1NGRmNjg2ODhlNDU3MDNiOTM2ODE4YTgyN2Q4ZTU0MGRkNmJlZjJlMTFlYzlkZGM2Y2ZlNWZjNzM2ZGQ3NjliOWY2ZTBhMjNhNjJlMmU1ZjQ5ZTg2MTQzNjQ2YTA0ZWMzYTIzZjgyODM3M2EzMzZhNWMyMjRhOTFmOGEwYzZjNmE3YjU4NDRkZDY0MTU4MDQyMDlmODNjOTQzYWVjYTljZmQ4NTZkYjZiZDRlYzMyMDA5YzhjYjI2OGVkMDUzMDUyYzkyMzdkZmQ4YmMKa2V5YmxvYl8wNCA9IDlmYmViMTk1N2ZjMTYyOWUwOGI3NTNhOTA4NmQ2ZTAxZmZiNGYxMTQ2NmI3NDE3ZTNmYTdmNWYxZWZiNzU0NDA2NzA0ZmQ3NWFmYWY5MWE0MDhhMGI1MjRjMWZjODBkMzZjMjA0NmZhNDc1NzQxMmVmZTRjMTFlMzgyZjcyZThhMTBkOTBlZDU4MDAxN2Q5ZGViODdhZjI1NDliNmIwMjY2MWFmNDhmZjk0ZjYwNzJjMGZlZjdmYzI4MzNiOGJkYWU1MDM4OThlMmU5MjdhYzA2NjNlOGI2MzkxZGQ0ZjFkNjg1MzEzOTM1ZTJjNDhlY2U3ZDE3N2M4OGJjOWM4ODNlZGUzNmMzNjc3NDk1Nzg0YjgzOGQ3MjY1YzZiYTdhMQprZXlibG9iXzA1ID0gOTRhOTJkYTFkNzNjMmIzZTE2NWM4OTFjZWQ1NjA3ZmM2NjI4Y2EyYTA2NTRmM2ZiYzA1NzExYzA2MzM3N2M2ZTljOTZhOWQwMTkyZTUzMGRkNTEwZTRmZDQxYWE2MmVmNDIxM2M1ZjZlMDU5ZTdlMjFkYjA5OGE5YjIyZDFlNmMyOWJlZTE0OGFhZWYxNWM1MjU0OWQ5MTY1ZGU5NmU4NWIwZDAyOWVjZGM1ODQzZTJmMzJjYjE4YmU3MDdlZWM2MTkwOWNmMzM4NWQ0NWJjMmE0YzhkNzZlOWJmYWQ1YTQwYzRiOTJkY2I5ODJhYTUwZDQ3NDg5N2FjOWViYjUzNTFhNzAxNWRjYzI3N2EwOGYxMjE0YWQ0MTM4NGQ3OTQxCmtleWJsb2Jfa2V5XzAwID0gODM5OTQ0YzhhMzhkZjY3OTEwMjBiMzgxNDdlOTA2YjAKa2V5YmxvYl9rZXlfMDEgPSBiOWU2ZmJkZTgyOGI1ZjQyYzg5N2FkZThmZDE0YzYyNQprZXlibG9iX2tleV8wMiA9IGI2OTg4YTA3OTVkMjk0ZWY1MjI5MDg2OTJkNWRiN2NhCmtleWJsb2Jfa2V5XzAzID0gMGU1N2Q3Nzc3MTcxZDEyNWQzZmUzYWY1YjM5N2QwMDkKa2V5YmxvYl9rZXlfMDQgPSBiNTVhMjgyZDY5OGZhYmViNGUwM2M2N2ZmMjAyNmJjNQprZXlibG9iX2tleV8wNSA9IGZkYjU0MmMxZjFiZGYxMzRlYzIwYjFmZGEwMmJjOWUxCmtleWJsb2Jfa2V5X3NvdXJjZV8wMCA9IGRmMjA2ZjU5NDQ1NGVmZGM3MDc0NDgzYjBkZWQ5ZmQzCmtleWJsb2Jfa2V5X3NvdXJjZV8wMSA9IDBjMjU2MTVkNjg0Y2ViNDIxYzIzNzllYTgyMjUxMmFjCmtleWJsb2Jfa2V5X3NvdXJjZV8wMiA9IDMzNzY4NWVlODg0YWFlMGFjMjhhZmQ3ZDYzYzA0MzNiCmtleWJsb2Jfa2V5X3NvdXJjZV8wMyA9IDJkMWY0ODgwZWRlY2VkM2UzY2YyNDhiNTY1N2RmN2JlCmtleWJsb2Jfa2V5X3NvdXJjZV8wNCA9IGJiNWEwMWY5ODhhZmY1ZmM2Y2ZmMDc5ZTEzM2MzOTgwCmtleWJsb2Jfa2V5X3NvdXJjZV8wNSA9IGQ4Y2NlMTI2NmEzNTNmY2MyMGYzMmQzYjUxN2RlOWMwCmtleWJsb2JfbWFjX2tleV8wMCA9IDYwNDQyMjUyNjcyM2U1NDFhODQ5ZmE0YzE4NjYwZTBiCmtleWJsb2JfbWFjX2tleV8wMSA9IDI3OTQ4MTQ1NmIxZGMyNTlkMzU1OTllNjM5MmUwMWU1CmtleWJsb2JfbWFjX2tleV8wMiA9IGRiYmZiODA5NmI2NzZjMmE1NGI1ZDljNjFiNDIzYTk0CmtleWJsb2JfbWFjX2tleV8wMyA9IDQ4YjdhZWY2ZDliMWVkYjEzMmI4OTAxYTI0NWE3NzUwCmtleWJsb2JfbWFjX2tleV8wNCA9IDU0NGMwODJlOWY4NjAyYzczNmRjMDczMmQ0MzE5Zjg4CmtleWJsb2JfbWFjX2tleV8wNSA9IGE1NDBlYzhiYTg0YmQzMWVhYWE5Y2U5Zjk1MjI2ODc1CmtleWJsb2JfbWFjX2tleV9zb3VyY2UgPSA1OWM3ZmI2ZmJlOWJiZTg3NjU2YjE1YzA1MzczMzZhNQptYXJpa29fbWFzdGVyX2tla19zb3VyY2VfMDUgPSA3NzYwNWFkMmVlNmVmODNjM2Y3MmUyNTk5ZGFjNWU1NgptYXJpa29fbWFzdGVyX2tla19zb3VyY2VfMDYgPSAxZTgwYjgxNzNlYzA2MGFhMTFiZTFhNGFhNjZmZTRhZQptYXJpa29fbWFzdGVyX2tla19zb3VyY2VfMDcgPSA5NDA4NjdiZDBhMDAzODg0MTFkMzFhZGJkZDhkZjE4YQptYXJpa29fbWFzdGVyX2tla19zb3VyY2VfMDggPSA1YzI0ZTNiOGI0ZjcwMGMyM2NmZDBhY2UxM2MzZGMyMwptYXJpa29fbWFzdGVyX2tla19zb3VyY2VfMDkgPSA4NjY5ZjAwOTg3YzgwNWFlYjU3YjQ4NzRkZTYyYTYxMwptYXJpa29fbWFzdGVyX2tla19zb3VyY2VfMGEgPSAwZTQ0MGNlZGI0MzZjMDNmYWExZGFlYmY2MmIxMDk4MgptYXJpa29fbWFzdGVyX2tla19zb3VyY2VfMGIgPSBlNTQxYWNlY2QxYTdkMWFiZWQwMzc3ZjEyN2NhZjhmMQptYXJpa29fbWFzdGVyX2tla19zb3VyY2VfMGMgPSA1MjcxOWJkZmE3OGI2MWQ4ZDU4NTExZTQ4ZTRmNzRjNgptYXJpa29fbWFzdGVyX2tla19zb3VyY2VfMGQgPSBkMjY4YzY1MzlkOTRmOWE4YTVhOGE3Yzg4ZjUzNGI3YQptYXN0ZXJfa2VrXzAwID0gZjc1OTAyNGY4MTk5MTAxZGRkYzFlZjkxZTZlZWNmMzcKbWFzdGVyX2tla18wMSA9IGJkMjcyNjRhZTA3ZTk3OTc1NjQxMWQwYzY2ZTY3OWUzCm1hc3Rlcl9rZWtfMDIgPSBhM2Q0YThlMTUzYjhlNmFlNmU2YWVmM2U4ZjIxOWNiNAptYXN0ZXJfa2VrXzAzID0gMTU1OGY1MjVhZThjNWJlOTI0M2ZiNmQ4YThiMGE4ZWUKbWFzdGVyX2tla18wNCA9IDlmYmViMTk1N2ZjMTYyOWUwOGI3NTNhOTA4NmQ2ZTAxCm1hc3Rlcl9rZWtfMDUgPSA5NGE5MmRhMWQ3M2MyYjNlMTY1Yzg5MWNlZDU2MDdmYwptYXN0ZXJfa2VrXzA4ID0gZTQyZjFlYzgwMDIwNDNkNzQ2NTc1YWU2ZGQ5ZjI4M2YKbWFzdGVyX2tla18wOSA9IGNlYzI4ODVmYmVlZjVmNmE5ODlkYjg0YTRjYzRiMzkzCm1hc3Rlcl9rZWtfMGEgPSBkZDFhNzMwMjMyNTIyYjVjYjQ1OTBjZDQzODY5YWI2YQptYXN0ZXJfa2VrXzBiID0gZmM2ZjBjODkxZDQyNzEwMTgwNzI0ZWQ5ZTExMmU3MmEKbWFzdGVyX2tla18wYyA9IDQzZjdmYzIwZmNlYzIyYTViMmE3NDQ3OTAzNzFiMDk0Cm1hc3Rlcl9rZWtfMGQgPSA4ZGM5YTgyMjM2NzFkYWE3M2NjZDhiOTNjZGFhZWQ5ZgptYXN0ZXJfa2VrX3NvdXJjZV8wNiA9IDM3NGI3NzI5NTliNDA0MzA4MWY2ZTU4YzZkMzYxNzlhCm1hc3Rlcl9rZWtfc291cmNlXzA3ID0gOWEzZWE5YWJmZDU2NDYxYzliZjY0ODdmNWNmYTA5NWMKbWFzdGVyX2tla19zb3VyY2VfMDggPSBkZWRjZTMzOTMwODgxNmY4YWU5N2FkZWM2NDJkNDE0MQptYXN0ZXJfa2VrX3NvdXJjZV8wOSA9IDFhZWMxMTgyMmIzMjM4N2EyYmVkYmEwMTQ3N2UzYjY3Cm1hc3Rlcl9rZWtfc291cmNlXzBhID0gMzAzZjAyN2VkODM4ZWNkNzkzMjUzNGI1MzBlYmNhN2EKbWFzdGVyX2tla19zb3VyY2VfMGIgPSA4NDY3YjY3ZjEzMTFhZWU2NTg5YjE5YWYxMzZjODA3YQptYXN0ZXJfa2VrX3NvdXJjZV8wYyA9IDY4M2JjYTU0Yjg2ZjkyNDhjMzA1NzY4Nzg4NzA3OTIzCm1hc3Rlcl9rZWtfc291cmNlXzBkID0gZjAxMzM3OWFkNTYzNTFjM2I0OTYzNWJjOWNlODc2ODEKbWFzdGVyX2tleV8wMCA9IGMyY2FhZmYwODliOWFlZDU1Njk0ODc2MDU1MjcxYzdkCm1hc3Rlcl9rZXlfMDEgPSA1NGUxYjhlOTk5YzJmZDE2Y2QwN2I2NjEwOWFjYWFhNgptYXN0ZXJfa2V5XzAyID0gNGY2YjEwZDMzMDcyYWYyZjI1MDU2MmJmZjA2YjZkYTMKbWFzdGVyX2tleV8wMyA9IDg0ZTA0ZWMyMGI5MzczODE4YzU0MDgyOWNmMTQ3ZjNkCm1hc3Rlcl9rZXlfMDQgPSBjZmEyMTc2NzkwYTUzZmY3NDk3NGJmZjJhZjE4MDkyMQptYXN0ZXJfa2V5XzA1ID0gYzFkYmVkY2ViZjBkZDY5NTYwNzllNTA2Y2ZhMWFmNmUKbWFzdGVyX2tleV8wNiA9IDBhYTkwZTYzMzBjZGMxMmQ4MTliMzI1NGQxMWE0ZTFlCm1hc3Rlcl9rZXlfMDcgPSA5MjlmODZmYmZlNGVmNzczMjg5MmJmMzQ2MjUxMWIwZQptYXN0ZXJfa2V5XzA4ID0gMjNjZmI3OTJjM2NiNTBjZDcxNWRhMGY4NDg4MGM4NzcKbWFzdGVyX2tleV8wOSA9IDc1YzkzYjcxNjI1NTMxOWI4ZTAzZTE0YzE5ZGVhNjRlCm1hc3Rlcl9rZXlfMGEgPSA3Mzc2NzQ4NGM3MzA4OGY2MjliMGVlYjYwNWY2NGFhNgptYXN0ZXJfa2V5XzBiID0gODUwMGIxNGJmNDc2NmI4NTVhMjZmZmM2MTQwOTdhOGYKbWFzdGVyX2tleV8wYyA9IGIzYzUwMzcwOTEzNWQ0YjM1ZGUzMWJlNGIwYjljMGY3Cm1hc3Rlcl9rZXlfMGQgPSA2ZDJiMjY0MTZhYjAzMGRjNTA0Y2JmZDZiYjI5NzdiNwptYXN0ZXJfa2V5X3NvdXJjZSA9IGQ4YTI0MTBhYzZjNTkwMDFjNjFkNmEyNjdjNTEzZjNjCnBhY2thZ2UxX2tleV8wMCA9IGY0ZWNhMTY4NWMxZTRkZjc3ZjE5ZGI3YjQ0YTk4NWNhCnBhY2thZ2UxX2tleV8wMSA9IGY4YzYwMzIyZjc1Y2Q1NDhiODIxYWY5MTYyZTE2Zjc2CnBhY2thZ2UxX2tleV8wMiA9IGM1ODBjYjFlMmQ5YWE5ODY2ZmZlZjkyMDAxMGZjNDA5CnBhY2thZ2UxX2tleV8wMyA9IGMzMjAwOWM4Y2IyNjhlZDA1MzA1MmM5MjM3ZGZkOGJjCnBhY2thZ2UxX2tleV8wNCA9IGVkZTM2YzM2Nzc0OTU3ODRiODM4ZDcyNjVjNmJhN2ExCnBhY2thZ2UxX2tleV8wNSA9IDFhNzAxNWRjYzI3N2EwOGYxMjE0YWQ0MTM4NGQ3OTQxCnBhY2thZ2UyX2tleV8wMCA9IGEzNWExOWNiMTQ0MDRiMmY0NDYwZDM0M2QxNzg2MzhkCnBhY2thZ2UyX2tleV8wMSA9IGEwZGQxZWFjZDQzODYxMGM4NWExOTFmMDJjMWRiOGE4CnBhY2thZ2UyX2tleV8wMiA9IDdlNWJhMmFhZmQ1N2Q0N2E4NWZkNGE1N2YyMDc2Njc5CnBhY2thZ2UyX2tleV8wMyA9IGJmMDNlOTg4OWZhMThmMGQ3YTU1ZThlOWY2ODQzMjNkCnBhY2thZ2UyX2tleV8wNCA9IDA5ZGY2ZTM2MWUyOGViOWM5NmM5ZmEwYmZjODk3MTc5CnBhY2thZ2UyX2tleV8wNSA9IDQ0NGIxYTRmOTAzNTE3OGI5YjFmZTI2MjQ2MmFjYjhlCnBhY2thZ2UyX2tleV8wNiA9IDQ0MmNkOWMyMWNmYjg5MTQ1ODdkYzEyZThlN2VkNjA4CnBhY2thZ2UyX2tleV8wNyA9IDcwYzgyMWU3ZDY3MTZmZWIxMjRhY2JhYzA5ZjdiODYzCnBhY2thZ2UyX2tleV8wOCA9IDhhY2NlYmNjM2QxNWEzMjhhNDgzNjU1MDNmODM2OWI2CnBhY2thZ2UyX2tleV8wOSA9IGY1NjJhN2M2YzQyZTNkNGQzZDEzZmZkNTA0ZDc3MzQ2CnBhY2thZ2UyX2tleV8wYSA9IDA4MDMxNjdlYzdmYzBiYzc1M2Q4MzMwZTU1OTJhMjg5CnBhY2thZ2UyX2tleV8wYiA9IDM0MWRiNjc5NmFhN2JkYjgwOTJmN2FhZTY1NTQ5MDBhCnBhY2thZ2UyX2tleV8wYyA9IDRlOTdkYzQyMjVkMDBjNmFlMzNkNDliZGRkMTc2MzdkCnBhY2thZ2UyX2tleV8wZCA9IGRiMTNjMmRlMmMzMTM1NDBiMThhMzJiNGYxMDZkNGExCnBhY2thZ2UyX2tleV9zb3VyY2UgPSBmYjhiNmE5Yzc5MDBjODQ5ZWZkMjRkODU0ZDMwYTBjNwpwZXJfY29uc29sZV9rZXlfc291cmNlID0gNGYwMjVmMGViNjZkMTEwZWRjMzI3ZDQxODZjMmY0NzgKcmV0YWlsX3NwZWNpZmljX2Flc19rZXlfc291cmNlID0gZTJkNmI4N2ExMTljYjg4MGU4MjI4ODhhNDZmYmExOTUKcnNhX29hZXBfa2VrX2dlbmVyYXRpb25fc291cmNlID0gYThjYTkzODQzNDEyN2ZkYTgyY2MxYWE1ZTgwN2IxMTIKcnNhX3ByaXZhdGVfa2VrX2dlbmVyYXRpb25fc291cmNlID0gZWYyY2I2MWE1NjcyOWI5MTU3YzM4YjkzMTY3ODRkZGQKc2F2ZV9tYWNfa2VrX3NvdXJjZSA9IGQ4OWMyMzZlYzkxMjRlNDNjODJiMDM4NzQzZjljZjFiCnNhdmVfbWFjX2tleSA9IDcxYTkxN2YxYmFjOGY0ZjA0ZDczMmU3MzRjOTBlMmVjCnNhdmVfbWFjX2tleV9zb3VyY2UgPSBlNGNkM2Q0YWQ1MGY3NDI4NDVhNDg3ZTVhMDYzZWExZgpzYXZlX21hY19zZF9jYXJkX2tla19zb3VyY2UgPSAwNDg5ZWY1ZDMyNmUxYTU5YzRiN2FiOGMzNjdhYWIxNwpzYXZlX21hY19zZF9jYXJkX2tleV9zb3VyY2UgPSA2ZjY0NTk0N2M1NjE0NmY5ZmZhMDQ1ZDU5NTMzMjkxOApzZF9jYXJkX2N1c3RvbV9zdG9yYWdlX2tleV9zb3VyY2UgPSAzNzBjMzQ1ZTEyZTRjZWZlMjFiNThlNjRkYjUyYWYzNTRmMmNhNWEzZmM5OTlhNDdjMDNlZTAwNDQ4NWIyZmQwCnNkX2NhcmRfa2VrX3NvdXJjZSA9IDg4MzU4ZDljNjI5YmExYTAwMTQ3ZGJlMDYyMWI1NDMyCnNkX2NhcmRfbmNhX2tleV9zb3VyY2UgPSA1ODQxYTI4NDkzNWI1NjI3OGI4ZTFmYzUxOGU5OWYyYjY3Yzc5M2YwZjI0ZmRlZDA3NTQ5NWRjYTAwNmQ5OWMyCnNkX2NhcmRfc2F2ZV9rZXlfc291cmNlID0gMjQ0OWI3MjI3MjY3MDNhODE5NjVlNmUzZWE1ODJmZGQ5YTk1MTUxN2IxNmU4ZjdmMWY2ODI2MzE1MmVhMjk2YQpzZF9zZWVkID0gZmRiNDc5MjIxYzQzNzQxYTExOGZiNTQ3NTM3NGQyZjcKc2VjdXJlX2Jvb3Rfa2V5ID0gMjA4ZGU5YjlkZTk0ZmY2OThkMDA2NTdhNmE4MmE5NzMKc3NsX3JzYV9rZWsgPSBiMDExMTAwNjYwZDFkY2NiYWQxYjFiNzMzYWZhOWY5NQpzc2xfcnNhX2tla19zb3VyY2VfeCA9IDdmNWJiMDg0N2IyNWFhNjdmYWM4NGJlMjNkN2I2OTAzCnNzbF9yc2Ffa2VrX3NvdXJjZV95ID0gOWEzODNiZjQzMWQwYmQ4MTMyNTM0YmE5NjQzOTdkZTMKdGl0bGVrZWtfMDAgPSA2MmEyNGQ2ZTZkMGQwZTBhYmYzNTU0ZDI1OWJlM2RjOQp0aXRsZWtla18wMSA9IDg4MjFmNjQyMTc2OTY5YjFhMTgwMjFkMjY2NWMwMTExCnRpdGxla2VrXzAyID0gNWQxNWI5Yjk1YTU3MzlhMGFjOWIyMGY2MDAyODM5NjIKdGl0bGVrZWtfMDMgPSAxYjNmNjNiY2I2N2Q0YjA2ZGE1YmFkYzdkODlhY2NlMQp0aXRsZWtla18wNCA9IGU0NWMxNzg5YTY5YzdhZmJiZjFhMWU2MWYyNDk5NDU5CnRpdGxla2VrXzA1ID0gZGRjNjdmNzE4OWY0NTI3YTM3YjUxOWNiMDUxZWVlMjEKdGl0bGVrZWtfMDYgPSBiMTUzMmI5ZDM4YWIwMzYwNjhmMDc0YzBkNzg3MDZhYwp0aXRsZWtla18wNyA9IDgxZGMxYjE3ODNkZjI2ODc4OWE2YTBlZGJmMDU4MzQzCnRpdGxla2VrXzA4ID0gNDdkZmU0YmYwZWVkYTg4YjE3MTM2YjgwMDVhYjA4ZWEKdGl0bGVrZWtfMDkgPSBhZGFhNzg1ZDkwZTFhOWMxODJhYzA3YmMyNzZiZjYwMAp0aXRsZWtla18wYSA9IDQyZGFhOTU3YzEyOGY3NWJiMWZkYTU2YTgzODdlMTdiCnRpdGxla2VrXzBiID0gZDA4OTAzMzYzZjJjODY1NWQzZGUzY2NmODVkNzk0MDYKdGl0bGVrZWtfMGMgPSBiZTI2ODI1OTlkYjM0Y2FhOWJjN2ViYjJjYzdjNjU0Ywp0aXRsZWtla18wZCA9IDQxMDcxZjk1YmVkZGM0MTE0YTAzZTAwNzJlNmNjYWI3CnRpdGxla2VrX3NvdXJjZSA9IDFlZGM3YjNiNjBlNmI0ZDg3OGI4MTcxNTk4NWU2MjliCnRzZWNfa2V5ID0gNTNlYzRhYzdjNmMzMmZmMmFiZmYzZWVmZjRmODRmMzYKdHNlY19yb290X2tleV8wMiA9IDRiNGZiY2Y1OGUyM2NmNDkwMmQ0NzhiNzZjODA0OGVjCg== "
siteCrypt = 'aHR0cHM6Ly9kYXJ0aHN0ZXJuaWUubmV0L3N3aXRjaC1maXJtd2FyZXMv'
welcomeScreen = """=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Welcome to the Yuzu auto-setup script.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
packageText = """1) What package are you using?
Supported packages: \x1B[3mFlatpak\x1B[0m
Planned packages: \x1B[3mWindows, AppImage\x1B[0m
"""
class color:
    ENDC = '\x1B[0m'
    INFO = '\033[93m'
def firmwareHelp():
    firmwareHelp = """??? ??? ???
    NOTE: If you want firmware files, do the following: \n1. download firmware from the link below.
    2. Move the firmware directory into the same place where firmware-install.py is \n3. Run firmware-install.py
    ??? ??? ???
    """
    firmware = input("Do you want instructions on firmware? y/n")
    if firmware in ["y", "Y", "yes", "Yes"]:
        print(firmwareHelp, str(base64.b64decode(siteCrypt).decode('utf-8')), "\n\n\n")
        return
    elif firmware in ["n", "N", "No", "no"]:
        print('\n\n\n')
        return
    else:
        print(color.INFO + "INFO 6:", "You did not specify correctly. The program will now exit.")
        print(color.INFO + "INFO 7:", firmware)
# -----------------------------

# yuzu setup installer - geck
# LICENSE: GPL-3.0-or-later
# NOTE: More packages planned in the future
# Supported packages
# - Flatpak

pkgType = []

print(welcomeScreen)
sleep(3)
print(packageText)

packageType = str(input("TYPE: "))

flatpak = ["Flatpak", "flatpak", "fp", "FP", "xdg_open"]
windows = ["Windows", "windows", "win", "win10", "Win", "Windows 10", "Windows 11"]
appimage = ["Appimage", "appimage", "AI", "ai", "AppImage", "PortableLinuxApps", "klik"]

if packageType in flatpak:
    print("Chose Flatpak")
    pkgType.append("FLATPAK")
elif packageType in windows:
    print("Chose Windows")
    pkgType.append("WINDOWS")
elif packageType in appimage:
    print("Chose AppImage")
    pkgType.append("APPIMAGE")
else:
    print("Error in packageType, the program will now exit.")
    print(color.INFO + "INFO 1:", packageType, color.ENDC) # Prints var packageType

print(color.INFO + "INFO 5:", pkgType, color.ENDC) # Prints var pkgType

if pkgType == ["FLATPAK"]:
    filecheck = os.path.isdir(os.getenv("HOME") + "/.var/app/org.yuzu_emu.yuzu/data")
    print(color.INFO + "INFO 3:", filecheck)  # Does the file exist?

    keyDecrypt = str(base64.b64decode(keyCrypt).decode('utf-8'))
    print(color.INFO + "INFO 4:", keyDecrypt[:50])  # Did decrypt work?

    keyCheck = os.path.exists(os.getenv("HOME") + "/.var/app/org.yuzu_emu.yuzu/data/yuzu/keys/prod.keys")
    print("INFO 6:", keyCheck)  # Does prod.keys already exist?
    if keyCheck:
        print("prod.keys already found. Please delete the file.")
    else:
        keyWrite = open(os.getenv("HOME") + "/.var/app/org.yuzu_emu.yuzu/data/yuzu/keys/prod.keys", "w")
        keyWrite.write(keyDecrypt)
        keyWrite.close()

        firmwareHelp()
        
        nextStep = 1
        
elif pkgType == ["APPIMAGE"]:
    filecheck = os.path.isdir(os.getenv("HOME") + "/.local/share/yuzu")
    print(color.INFO + "INFO 3:", filecheck)  # Does the file exist?
    
    keyDecrypt = str(base64.b64decode(keyCrypt).decode('utf-8'))
    print(color.INFO + "INFO 4:", keyDecrypt[:50])  # Did decrypt work?
    
    keyCheck = os.path.exists(os.getenv("HOME") + "/.local/share/yuzu/keys/prod.keys")
    print("INFO 6:", keyCheck)  # Does prod.keys already exist?
    if keyCheck:
        print("prod.keys already found. Please delete the file.")
    else:
        keyWrite = open(os.getenv("HOME") + "/.local/share/yuzu/keys/prod.keys", "w")
        keyWrite.write(keyDecrypt)
        keyWrite.close()

        firmwareHelp()
        
        nextStep = 1
else:
    print(color.INFO + "INFO 9:", "Error", color.ENDC) # Error, usually typing

if nextStep == 1:
    print("-=- CUSTOMIZATION -=-")
    # Yes I realize this code is repeated and probably a waste of space, but it works so im keeping it

    gpu = str(input("Do you have a NVIDIA, AMD or INTEL GPU?\n TYPE: "))
    if gpu in ['NVIDIA', 'AMD', 'INTEL']:
        sf = "backend=0"
        sf2 = "backend\default=true"
        rt = "backend=1"
        rt2 = "backend\default=false"
        with open(os.getenv("HOME") + "/.var/app/org.yuzu_emu.yuzu/config/yuzu/qt-config.ini", 'r') as file:
            data = file.read()
            data = data.replace(sf, rt)
            data = data.replace(sf2, rt2)
        with open(os.getenv("HOME") + "/.var/app/org.yuzu_emu.yuzu/config/yuzu/qt-config.ini", 'w') as file:
            file.write(data)
        print("Done.")
    try:
        gpu
    except NameError:
        print("GPU isn't defined, error.")
    else:
        sf = "gpu_accuracy=1"
        sf2 = "gpu_accuracy\default=true"
        rt = "gpu_accuracy=0"
        rt2 = "gpu_accuracy\default=false"
        with open(os.getenv("HOME") + "/.var/app/org.yuzu_emu.yuzu/config/yuzu/qt-config.ini", 'r') as file:
            data = file.read()
            data = data.replace(sf, rt)
            data = data.replace(sf2, rt2)
        with open(os.getenv("HOME") + "/.var/app/org.yuzu_emu.yuzu/config/yuzu/qt-config.ini", 'w') as file:
            file.write(data)
        print("Done.")
    print("Do you have these monitor sizes?")
    monitor = str(input("Possible values: 1440, 4k, none"))
    if monitor == '1440':
        sf = "resolution_setup=2"
        sf2 = "resolution_setup\default=true"
        rt = "resolution_setup=3"
        rt2 = "resolution_setup\default=false"
        with open(os.getenv("HOME") + "/.var/app/org.yuzu_emu.yuzu/config/yuzu/qt-config.ini", 'r') as file:
            data = file.read()
            data = data.replace(sf, rt)
            data = data.replace(sf2, rt2)
        with open(os.getenv("HOME") + "/.var/app/org.yuzu_emu.yuzu/config/yuzu/qt-config.ini", 'w') as file:
            file.write(data)
        print("Done.")
    elif monitor == '4k':
        sf = "resolution_setup=2"
        sf2 = "resolution_setup\default=true"
        rt = "resolution_setup=4"
        rt2 = "resolution_setup\default=false"
        with open(os.getenv("HOME") + "/.var/app/org.yuzu_emu.yuzu/config/yuzu/qt-config.ini", 'r') as file:
            data = file.read()
            data = data.replace(sf, rt)
            data = data.replace(sf2, rt2)
        with open(os.getenv("HOME") + "/.var/app/org.yuzu_emu.yuzu/config/yuzu/qt-config.ini", 'w') as file:
            file.write(data)
        print("Done.")
    else:
        pass
else:
    print(color.INFO + "INFO 9:", "Error", color.ENDC) # Error, usually typing

print("Install completed.")

# aaaa