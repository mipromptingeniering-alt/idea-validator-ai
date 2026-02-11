#!/usr/bin/env python3
"""
Metrics Tracker - Sistema de seguimiento de métricas
CORREGIDO: Manejo robusto de columnas
"""
import pandas as pd
import time
import os
from datetime import datetime
from collections import Counter

def track_metrics():
    csv_path = 'data/ideas-validadas.csv'

    if not os.path.exists(csv_path):
        print("⚠️  CSV no encontrado. Esperando ideas...")
        return

    try:
        df = pd.read_csv(csv_path, encoding='utf-8-sig')

        if df.empty:
            print("📊 No hay ideas aún. Esperando...")
            return

        # Calcular métricas básicas
        total_ideas = len(df)
        avg_score = round(df['Score Total'].mean(), 1) if 'Score Total' in df.columns else 0
        top_performers = len(df[df['Score Total'] > 70]) if 'Score Total' in df.columns else 0

        # Por tipo
        tipo_counts = Counter(df['Tipo']) if 'Tipo' in df.columns else Counter()

        # Deployed - manejo robusto
        deployed = 0
        if 'Landing Deployed' in df.columns:
            deployed = len(df[df['Landing Deployed'].astype(str).str.lower() == 'sí'])
        elif 'Landing URL' in df.columns:
            # Contar URLs no vacías
            deployed = len(df[df['Landing URL'].astype(str).str.strip() != ''])

        print("\n" + "="*60)
        print(f"📊 MÉTRICAS - {datetime.now().strftime('%H:%M:%S')}")
        print("="*60)
        print(f"Total Ideas:      {total_ideas}")
        print(f"Score Promedio:   {avg_score}/100")
        print(f"Top Performers:   {top_performers} (score > 70)")
        print(f"Deployed:         {deployed}")

        if tipo_counts:
            print(f"\nPor Tipo:")
            for tipo, count in tipo_counts.most_common():
                print(f"  {tipo:15s}: {count}")

        print("="*60)

    except Exception as e:
        print(f"❌ Error actualizando métricas: {e}")

def run_tracker():
    print("📊 METRICS TRACKER INICIADO")
    print("   Actualiza cada 60 segundos\n")

    while True:
        try:
            track_metrics()
            time.sleep(60)
        except KeyboardInterrupt:
            print("\n🛑 TRACKER DETENIDO")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(60)

if __name__ == '__main__':
    run_tracker()
