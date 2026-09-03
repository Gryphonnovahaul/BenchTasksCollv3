#!/usr/bin/env python3
import subprocess, os, shutil
SRC = {
  "activity-logger": [
    "lueyang-dev",
    "lueyang"
  ],
  "alert-system": [
    "yuzhen-dev",
    "yuzhen"
  ],
  "analytics-dashboard": [
    "lv",
    "lv"
  ],
  "asset-optimizer": [
    "yuxuan-dev",
    "yuxuan"
  ],
  "backup-utility": [
    "xiaochen_dev",
    "xiaochen"
  ],
  "blog-engine": [
    "gyy",
    "gyy"
  ],
  "booking-system": [
    "junteng_dev",
    "junteng"
  ],
  "cache-optimizer": [
    "wenshuo-dev",
    "wenshuo"
  ],
  "certificate-manager": [
    "zhaochen",
    "zhaochen"
  ],
  "chat-bot": [
    "lv",
    "lv"
  ],
  "client-portal": [
    "lueyang-dev",
    "lueyang"
  ],
  "cms-builder": [
    "gyy",
    "gyy"
  ],
  "contact-manager": [
    "junteng_dev",
    "junteng"
  ],
  "content-manager": [
    "yuxuan-dev",
    "yuxuan"
  ],
  "content-scheduler": [
    "gyy",
    "gyy"
  ],
  "coupon-manager": [
    "fan-dev",
    "fan"
  ],
  "crm-system": [
    "lueyang-dev",
    "lueyang"
  ],
  "customer-feedback-processor": [
    "jl_dev",
    "jl"
  ],
  "customer-portal": [
    "junteng_dev",
    "junteng"
  ],
  "data-analytics": [
    "ruige",
    "ruige"
  ],
  "data-validator": [
    "yuzhen-dev",
    "yuzhen"
  ],
  "deal-manager": [
    "lueyang-dev",
    "lueyang"
  ],
  "deployment-tool": [
    "xiaochen_dev",
    "xiaochen"
  ],
  "discount-calculator": [
    "fan-dev",
    "fan"
  ],
  "email-campaign": [
    "lueyang-dev",
    "lueyang"
  ],
  "email-classification-system": [
    "jl_dev",
    "jl"
  ],
  "error-tracker": [
    "xiaochen_dev",
    "xiaochen"
  ],
  "expense-tracker": [
    "ruige",
    "ruige"
  ],
  "feedback-collector": [
    "lv",
    "lv"
  ],
  "file-manager": [
    "ruige",
    "ruige"
  ],
  "follow-up-reminder": [
    "lueyang-dev",
    "lueyang"
  ],
  "form-builder": [
    "yuzhen-dev",
    "yuzhen"
  ],
  "health-monitor": [
    "xiaochen_dev",
    "xiaochen"
  ],
  "help-desk": [
    "junteng_dev",
    "junteng"
  ],
  "image-processor": [
    "wenshuo-dev",
    "wenshuo"
  ],
  "inventory-management": [
    "jl_dev",
    "jl"
  ],
  "invoice-generator": [
    "yuzhen-dev",
    "yuzhen"
  ],
  "load-balancer": [
    "zhaochen",
    "zhaochen"
  ],
  "log-analyzer": [
    "ruige",
    "ruige"
  ],
  "loyalty-program": [
    "fan-dev",
    "fan"
  ],
  "media-organizer": [
    "haoze",
    "haoze"
  ],
  "monitoring-agent": [
    "xiaochen_dev",
    "xiaochen"
  ],
  "network-analyzer": [
    "yuxuan-dev",
    "yuxuan"
  ],
  "order-processor": [
    "junteng_dev",
    "junteng"
  ],
  "payment-processor": [
    "yuzhen-dev",
    "yuzhen"
  ],
  "pdf-report-generator": [
    "jl_dev",
    "jl"
  ],
  "permission-manager": [
    "yuzhen-dev",
    "yuzhen"
  ],
  "personalization-service": [
    "lv",
    "lv"
  ],
  "price-tracker": [
    "fan-dev",
    "fan"
  ],
  "product-catalog": [
    "junteng_dev",
    "junteng"
  ],
  "qr-generator": [
    "junxian_dev",
    "junxian"
  ],
  "reminder-service": [
    "junteng_dev",
    "junteng"
  ],
  "robots-handler": [
    "gyy",
    "gyy"
  ],
  "sales-pipeline": [
    "lueyang-dev",
    "lueyang"
  ],
  "scheduler": [
    "wenshuo-dev",
    "wenshuo"
  ],
  "search-engine": [
    "wenshuo-dev",
    "wenshuo"
  ],
  "security-scanner": [
    "xiaochen_dev",
    "xiaochen"
  ],
  "sentiment-analyzer": [
    "lv",
    "lv"
  ],
  "shipment-tracker": [
    "junteng_dev",
    "junteng"
  ],
  "sitemap-generator": [
    "gyy",
    "gyy"
  ],
  "social-connector": [
    "junxian_dev",
    "junxian"
  ],
  "social-publisher": [
    "gyy",
    "gyy"
  ],
  "status-checker": [
    "xiaochen_dev",
    "xiaochen"
  ],
  "storage-manager": [
    "zhaochen",
    "zhaochen"
  ],
  "streaming-service": [
    "haoze",
    "haoze"
  ],
  "survey-builder": [
    "lv",
    "lv"
  ],
  "sync-service": [
    "yuxuan-dev",
    "yuxuan"
  ],
  "tag-manager": [
    "gyy",
    "gyy"
  ],
  "task-scheduler": [
    "yuxuan-dev",
    "yuxuan"
  ],
  "template-engine": [
    "zhaochen",
    "zhaochen"
  ],
  "territory-manager": [
    "lueyang-dev",
    "lueyang"
  ],
  "translation-api": [
    "junxian_dev",
    "junxian"
  ],
  "video-trimmer": [
    "haoze",
    "haoze"
  ],
  "voice-processor": [
    "lv",
    "lv"
  ],
  "web-crawler": [
    "ruige",
    "ruige"
  ],
  "canvas-automation": [
    "ruige",
    "ruige"
  ],
  "canvas-grade-automation": [
    "jl_dev",
    "jl"
  ],
  "calendar-sync": [
    "junteng_dev",
    "junteng"
  ]
}
os.makedirs("tasks/finalpool", exist_ok=True)
subprocess.run(["git","fetch","--all","--quiet"], check=True)
for task,(branch,dev) in SRC.items():
    src=f"tasks/{dev}/{task}"
    dst=f"tasks/finalpool/{task}"
    r=subprocess.run(["git","ls-tree","-r","--name-only",f"origin/{branch}",src],capture_output=True,text=True)
    files=[l for l in r.stdout.splitlines() if l.startswith(src+"/")]
    if not files:
        print("MISSING", task, branch, dev); continue
    for f in files:
        rel=f[len(src)+1:]
        out=os.path.join(dst,rel)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        content=subprocess.run(["git","show",f"origin/{branch}:{f}"],capture_output=True,check=True).stdout
        open(out,"wb").write(content)
    print("copied", task, len(files))
print("TASKS DONE", len(SRC))
