import SparklesIcon from "@/components/SparklesIcon";

export default function DemoSection() {
  return (
    <section className="flex justify-around mt-8 sm:mt-12 items-center">
      <div className="hidden sm:block bg-gray-800/50 w-[240px] rounded-xl overflow-hidden">
        <video src="https://caption-aniket.s3.eu-north-1.amazonaws.com/Mark+Zuckerberg+shorts.mp4" preload muted autoPlay loop></video>
      </div>
      <div className="hidden sm:block">
        <SparklesIcon />
      </div>
      <div className="bg-gray-800/50 w-[240px] rounded-xl overflow-hidden">
        <video src="https://caption-aniket.s3.eu-north-1.amazonaws.com/mark+caption.mp4" preload muted autoPlay loop></video>
      </div>
    </section>
  );
}